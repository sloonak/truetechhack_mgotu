$(document).ready(function () {
    const videoPlayer = document.getElementById('videoPlayer');
    var json = getTimeIntervalsEpileptic();

    videoPlayer.addEventListener('timeupdate', function () {
        const currentTime = videoPlayer.currentTime;

        intervals = json.result[3];
        max = intervals.length;

        for (let i = 0; i < max; i++) {
            if(currentTime < intervals[i]['end'] && currentTime > intervals[i]['start']) {
                // TODO: сделать обновление яркости и контрасности для canvas
                
            }
        }
    });

    function getTimeIntervalsEpileptic() {
        // Замените your_api_endpoint на URL-адрес конечной точки API на вашем сервере.
        const apiUrl = '/service/get_analyze';
        var json = '';
        url = '/var/www/truetechhack/static/video/rik1080.mp4';

        result = $.post({
            type: 'POST',
            url: apiUrl,
            data: JSON.stringify({ action: 'analyze', url: url }),
            contentType: 'application/json',
            async: false,
            ajax: false,
            success: function (response) {
                json = response;
            },
            error: function (error) {
                console.error(error);
            }
        });

        return json;
    }
});
