# **Preprocessing**

# Deep Learning and Image Recognition
  1. Using ESP32-CAM ([Ref1](https://youyouyou.pixnet.net/blog/post/119383183#google_vignette), [Ref2](https://www.nmking.io/index.php/2022/11/03/422/))
  2. Install **Arduino IDE** ([download](https://www.arduino.cc/en/software/#ide))
  3. Open **Arduino IDE** --> choose **file/preferences** --> in **addition boards manager URL** enter "https://dl.espressif.com/dl/package_esp32_index.json"
  4. Choose **Tools/Board** --> choose **Board...** --> choose **ESP32 Wrover Module**
  5. Execute the [command](https://github.com/Anran13/python/blob/main/MQTT_CAM_OK_upload.ino) in **Arduino IDE**
  6. Go to [MQTT GO](https://broker.mqttgo.io/) and link to our camera.
  7. Choose **Add Subscription** and set **儀錶板** to **圖片**