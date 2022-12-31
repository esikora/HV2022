# Used by hv22_11_screenshot_ocr.py

# Symbol, Filename, Threshold
symbols = [
    ('"', "34.png", 0.8),
    ('"', "34_2.png", 0.8),
    ("+", "43.png", 0.9),
    (",", "44.png", 0.8),
    (",", "44_2.png", 0.8),
    ("-", "45.png", 0.8),
    ("/", "47.png", 0.9),
    ("/", "47_2.png", 0.9),
    ("0", "48.png", 0.9),
    ("0", "48_2.png", 0.9),
    ("1", "49.png", 0.9),
    ("1", "49_2.png", 0.9),
    ("2", "50.png", 0.9),
    ("2", "50_2.png", 0.9),
    ("3", "51.png", 0.8),
    ("4", "52.png", 0.8),
    ("5", "53.png", 0.9),
    ("5", "53_2.png", 0.9),
    ("6", "54.png", 0.8),
    ("7", "55.png", 0.8),
    ("8", "56.png", 0.9),
    ("8", "56_2.png", 0.9),
    ("9", "57.png", 0.8),
    ("9", "57_2.png", 0.8),
    (":", "58.png", 0.8),
    (":", "58_2.png", 0.8),
    ("=", "61.png", 0.95),
    ("A", "65.png", 0.8),
    ("A", "65_2.png", 0.8),
    ("B", "66.png", 0.9),
    ("B", "66_2.png", 0.9),
    ("C", "67.png", 0.85),
    ("C", "67_2.png", 0.85),
    ("D", "68.png", 0.9),
    ("D", "68_2.png", 0.9),
    ("E", "69.png", 0.85),
    ("F", "70.png", 0.9),
    ("F", "70_2.png", 0.9),
    ("G", "71.png", 0.85),
    ("G", "71_2.png", 0.85),
    ("H", "72.png", 0.85),
    ("H", "72_2.png", 0.85),
    ("H", "72_3.png", 0.85),
    ("I", "73.png", 0.95),
    ("I", "73_2.png", 0.95),
    ("I", "73_3.png", 0.95),
    ("I", "73_4.png", 0.95),
    ("I", "73_5.png", 0.95),
    ("J", "74.png", 0.85),
    ("J", "74_2.png", 0.85),
    ("K", "75.png", 0.85),
    ("K", "75_2.png", 0.85),
    ("L", "76.png", 0.85),
    ("L", "76_2.png", 0.85),
    ("M", "77.png", 0.8),
    ("M", "77_2.png", 0.8),
    ("N", "78.png", 0.8),
    ("N", "78_2.png", 0.8),
    ("O", "79.png", 0.96),
    ("O", "79_2.png", 0.96),
    ("O", "79_3.png", 0.96),
    ("O", "79_4.png", 0.96),
    ("P", "80.png", 0.9),
    ("P", "80_2.png", 0.9),
    ("Q", "81.png", 0.96),
    ("Q", "81_2.png", 0.96),
    ("Q", "81_3.png", 0.96),
    ("Q", "81_4.png", 0.96),
    ("R", "82.png", 0.9),
    ("R", "82_2.png", 0.9),
    ("S", "83.png", 0.85),
    ("T", "84.png", 0.9),
    ("T", "84_2.png", 0.9),
    ("U", "85.png", 0.85),
    ("U", "85_2.png", 0.85),
    ("V", "86.png", 0.9),
    ("V", "86_2.png", 0.9),
    ("W", "87.png", 0.8),
    ("W", "87_2.png", 0.8),
    ("X", "88.png", 0.85),
    ("X", "88_2.png", 0.85),
    ("Y", "89.png", 0.8),
    ("Y", "89_2.png", 0.8),
    ("Z", "90.png", 0.8),
    ("a", "97.png", 0.9),
    ("a", "97_2.png", 0.9),
    ("b", "98.png", 0.9),
    ("b", "98_2.png", 0.9),
    ("c", "99.png", 0.9),
    ("c", "99_2.png", 0.9),
    ("d", "100.png", 0.9),
    ("d", "100_2.png", 0.9),
    ("e", "101.png", 0.85),
    ("e", "101_2.png", 0.85),
    ("f", "102.png", 0.9),
    ("f", "102_2.png", 0.9),
    ("g", "103.png", 0.9),
    ("g", "103_2.png", 0.9),
    ("h", "104.png", 0.95),
    ("h", "104_2.png", 0.95),
    ("h", "104_3.png", 0.95),
    ("h", "104_4.png", 0.95),
    ("i", "105.png", 0.95),
    ("i", "105_2.png", 0.95),
    ("i", "105_3.png", 0.95),
    ("i", "105_4.png", 0.95),
    ("j", "106.png", 0.9),
    ("j", "106_2.png", 0.9),
    ("j", "106_3.png", 0.9),
    ("k", "107.png", 0.9),
    ("k", "107_2.png", 0.9),
    ("l", "108.png", 0.96),
    ("l", "108_2.png", 0.96),
    ("l", "108_3.png", 0.96),
    ("l", "108_4.png", 0.96),
    ("l", "108_5.png", 0.96),
    ("l", "108_6.png", 0.96),
    ("m", "109.png", 0.9),
    ("m", "109_2.png", 0.9),
    ("n", "110.png", 0.95),
    ("n", "110_2.png", 0.95),
    ("n", "110_3.png", 0.95),
    ("n", "110_4.png", 0.95),
    ("n", "110_5.png", 0.95),
    ("o", "111.png", 0.9),
    ("o", "111_2.png", 0.9),
    ("p", "112.png", 0.9),
    ("p", "112_2.png", 0.9),
    ("q", "113.png", 0.9),
    ("q", "113_2.png", 0.9),
    ("r", "114.png", 0.95),
    ("r", "114_2.png", 0.95),
    ("r", "114_3.png", 0.95),
    ("r", "114_4.png", 0.95),
    ("s", "115.png", 0.9),
    ("s", "115_2.png", 0.9),
    ("t", "116.png", 0.9),
    ("t", "116_2.png", 0.9),
    ("u", "117.png", 0.9),
    ("u", "117_2.png", 0.9),
    ("v", "118.png", 0.9),
    ("v", "118_2.png", 0.9),
    ("w", "119.png", 0.9),
    ("w", "119_2.png", 0.9),
    ("x", "120.png", 0.9),
    ("x", "120_2.png", 0.9),
    ("y", "121.png", 0.9),
    ("y", "121_2.png", 0.9),
    ("y", "121_3.png", 0.9),
    ("z", "122.png", 0.9),
    ("z", "122_2.png", 0.9),
    ("{", "123.png", 0.8),
    ("}", "125.png", 0.8)
]
