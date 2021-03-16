# Shadding attenuation algorithm 💻🧬
## (with DullRazor algorithm)
<img src="screenshots/screenshot_0.png" alt="homepage"><br>
<hr>

### Minimum equirements 

<p>Programming language: <i>Python</i><br>
Version language: <i>Python 3.8.8</i><br>
Libraries: <i>OpenCV 4.5.1, Numpy 1.19.2</i><br>
</p>
<hr>

<p style="text-align:justify;">The human body is made up of curved surfaces that make the light projected on it not uniform. This circularity creates shadows and adds noise to dermoscopic images, making it difficult to segment the lesion. According to Cavalcanti et al., It is possible to attenuate the shadows present in this type of images by means of a linear regression in 2-D, modeling the variations in lighting and reassigning the values of each pixel.</p>

<p style="text-align:justify;">Taking into account that there are no abrupt changes in the illumination of the image, this variation can be modeled by means of a quadratic function or second degree polynomial. To approximate the coefficients of the polynomial, it is necessary to use the pixels that have more information about the shadows, that is, those found in the corners of the image. Consequently, a set of 20 × 20 pixels is extracted from each corner and a matrix 𝑆 is formed containing the union of the four sets (n = 1600 pixels). Then the matrix 𝑆 is used to approximate the coefficients of the quadratic function 𝑧 (𝑥, 𝑦):</p>

<p style="text-align:center;">𝑧(𝑥,𝑦)=𝑝<sub>1</sub>x<sup>2</sup>+𝑝<sub>2</sub>y<sup>2</sup>+𝑝<sub>3</sub>𝑥𝑦+𝑝<sub>4</sub>𝑥+𝑝<sub>5</sub>𝑦+𝑝<sub>6</sub></p>

<p style="text-align:justify;">Where the variables 𝑥 and 𝑦 correspond to the coordinates of each element of 𝑆.</p>

<p style="text-align:justify;">As the number of pixels is not large, the method of ordinary least squares (OLS) is used to minimize the function 𝑧 (𝑥, 𝑦), and find the parameters 𝑝<sub>1</sub> ⋯ 𝑝<sub>6</sub>. This method is not iterative and therefore has less computational requirements. The expression for OLS, in its matrix form, is given by the following equation:</p>

<p style="text-align:center;">𝛽=(𝑋<sup>T</sup>𝑋)<sup>-1</sup>𝑋<sup>T</sup>𝑦</p>

<p style="text-align:justify;">Where 𝛽 is the resulting 6 × 1 matrix containing the coefficients 𝑝<sub>1</sub> ⋯ 𝑝<sub>6</sub>, 𝑋 is an n × 6 matrix with the terms for each coordinate (𝑥, 𝑦), and 𝑦 is an n × 1 matrix containing the intensity values of each pair (𝑥, 𝑦).</p>

<p style="text-align:justify;">Once the coefficients have been obtained, 𝑧 (𝑥, 𝑦) is calculated for each pixel of the blue channel of the image, in order to estimate the intensity of local illumination. Finally, the shadows are attenuated by the following expression:</p>

<p style="text-align:center;">𝑅(𝑥,𝑦)=𝐼(𝑥,𝑦)/𝑧(𝑥,𝑦)</p>

<p style="text-align:justify;">Where 𝑅 (𝑥, 𝑦) is the resulting image, 𝐼 (𝑥, 𝑦) the blue layer of the image and 𝑧 (𝑥, 𝑦) the local illumination intensity obtained.</p>

<p style="text-align:justify;">This algorithm use DullRazor technique. To see the algorithm click <a href="https://github.com/BlueDokk/Dullrazor-algorithm" target="blank">[here]</a></p>

<hr>

## SCREENSHOTS

<p>Input image from HAM10000 database.</p>

### Input image
<img src="screenshots/screenshot_1.png" alt="Input image"><br>

### Cropped image
<img src="screenshots/screenshot_2.png" alt="Cropped image"><br>

### DullRazor
<img src="screenshots/screenshot_6.png" alt="Dullrazor"><br>

### Blue channel
<img src="screenshots/screenshot_3.png" alt="Blue channel"><br>

### Attenuator element
<img src="screenshots/screenshot_4.png" alt="Attenuator element"><br>

### Shadding attenuation on image (Output image)
<img src="screenshots/screenshot_5.png" alt="Output image"><br>

<p><i>Developed by engineer Javier Velasquez (2020)</i></p>
