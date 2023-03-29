$(document).ready(function () {
    var video = document.getElementById('videoPlayer');
    var canvas = document.getElementById('canvas1');
    var ctx = canvas.getContext('2d');

    function resize_canvas(element)
    {
     var w = element.offsetWidth;
      var h = element.offsetHeight;
      var cv = document.getElementById("canvas1");
      cv.width = w;
      cv.height =h;
    }

    resize_canvas(document.getElementById("videoPlayer"));

    video.addEventListener('loadeddata', function() {
        // Запускаем воспроизведение видео
        video.play();

        // Создаем функцию, которая будет выполняться на каждом кадре видео
        function draw() {
          // Отрисовываем текущий кадр видео на canvas
          ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

          // Накладываем маску на canvas
          ctx.fillStyle = 'rgba(255, 255, 255, 0)';
          ctx.fillRect(0, 0, canvas.width, canvas.height);

          // Получаем данные пикселей на canvas
          var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
          var data = imageData.data;

          // Применяем эффект яркости и контрастности к данным пикселей
          var brightness = -30;
          var contrast = 0.5;
          for (var i = 0; i < data.length; i += 4) {
            var red = data[i];
            var green = data[i + 1];
            var blue = data[i + 2];

            // Применяем яркость
            red += brightness;
            green += brightness;
            blue += brightness;

            // Применяем контрастность
            red = Math.floor(((red / 255 - 0.5) * contrast + 0.5) * 255);
            green = Math.floor(((green / 255 - 0.5) * contrast + 0.5) * 255);
            blue = Math.floor(((blue / 255 - 0.5) * contrast + 0.5) * 255);

            // Ограничиваем значения RGB до диапазона [0, 255]
            red = Math.max(0, Math.min(255, red));
            green = Math.max(0, Math.min(255, green));
            blue = Math.max(0, Math.min(255, blue));

            // Записываем обновленные значения RGB обратно в данные пикселей
            data[i] = red;
            data[i + 1] = green;
            data[i + 2] = blue;
          }

          // Записываем обновленные данные пикселей обратно на canvas
          ctx.putImageData(imageData, 0, 0);

          // Запускаем функцию draw() на следующем кадре видео
         
      requestAnimationFrame(draw);
    }

    // Запускаем функцию draw() на первом кадре видео
    draw();
    });
});

