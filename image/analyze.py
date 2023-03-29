import cv2
import concurrent.futures
from PIL import Image, ImageStat

def read_frames(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame

def analyze_frames(frames, start_frame, avg_brightness, avg_contrast):
    epilepsy_intervals = []
    current_interval = None

    for i, frame_info in enumerate(frames):
        contrast = frame_info["contrast"]
        brightness = frame_info["brightness"]

        if contrast > avg_contrast and brightness > avg_brightness:
            if not current_interval:
                current_interval = (i, i, frame_info)
            else:
                current_interval = (current_interval[0], i, frame_info)
        else:
            if current_interval:
                epilepsy_intervals.append(current_interval)
                current_interval = None

    if current_interval:
        epilepsy_intervals.append(current_interval)

    return epilepsy_intervals

def calculate_average_brightness_contrast(frames):
    avg_contrast = sum(frame["contrast"] for frame in frames) / len(frames)
    avg_brightness = sum(frame["brightness"] for frame in frames) / len(frames)
    return avg_brightness, avg_contrast

def process_frame_brightness_contrast(frame):
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    contrast = ImageStat.Stat(img).rms[0]
    brightness = ImageStat.Stat(img.convert('L')).mean[0]
    return {"contrast": contrast, "brightness": brightness}

def process_video_segment(segment_start, segment_end, avg_brightness, avg_contrast):
    local_cap = cv2.VideoCapture(video_path)
    local_cap.set(cv2.CAP_PROP_POS_FRAMES, segment_start)
    frames = []

    for _ in range(segment_start, segment_end):
        ret, frame = local_cap.read()
        if not ret:
            break

        frame_data = process_frame_brightness_contrast(frame)
        frames.append(frame_data)

    local_cap.release()
    epilepsy_intervals = analyze_frames(frames, 0, avg_brightness, avg_contrast)
    return (segment_start, epilepsy_intervals)

def analyze_video(url): 
    video_path = url
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate average brightness and contrast for the entire video
    all_frames = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        frame_results = list(executor.map(process_frame_brightness_contrast, read_frames(cap)))

    cap.release()
    avg_brightness, avg_contrast = calculate_average_brightness_contrast(frame_results)

    num_threads = 4
    segment_duration = int(total_frames / num_threads)
    futures = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            segment_start = i * segment_duration
            segment_end = (i + 1) * segment_duration if i < num_threads - 1 else total_frames
            futures.append(executor.submit(process_video_segment, segment_start, segment_end, avg_brightness, avg_contrast))

    all_epilepsy_intervals = []
    for future in concurrent.futures.as_completed(futures):
        segment_start, epilepsy_intervals = future.result()
        adjusted_intervals = [(interval[0] + segment_start, interval[1] + segment_start, interval[2]) for interval in epilepsy_intervals]
        all_epilepsy_intervals.extend(adjusted_intervals)

    data = []
    for interval in all_epilepsy_intervals:
        start_time = round(interval[0] / fps, 6)
        end_time = round(interval[1] / fps, 6)
        brightness = round(100 * (1 - interval[2]["brightness"] / avg_brightness), 2),
        contrast = round(100 * (1 - interval[2]["contrast"] / avg_contrast), 2),
        
        data.append({'start': start_time, 'end': end_time, "brightness": brightness, "contrast": contrast})

    cap.release()
    return data