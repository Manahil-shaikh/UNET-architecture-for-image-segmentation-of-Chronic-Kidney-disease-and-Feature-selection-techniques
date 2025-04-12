Introduction to Project:
Chronic kidney disease (CKD) refers to any long-term condition which deteriorates the functionality of the kidney in body waste filtration. The disease could be treated if diagnosed timely. Keeping this problem domain in view, the proposed approach includes adaptive machine-learning techniques for chronic kidney disease detection to trace the infected areas and create a base for kidney image analysis. Furthermore, we will process the CT scan images of the Kidney to determine the abnormality. Moreover, our technique includes promising opportunities as it can further be modified into a wearable device. Also, it can play a considerable role in a patient's health care and diagnostics.

Feature-selection-and-model-prediction:
The model is also modified to reduce the computational cost. The dense full file contains a modified UNET model, which includes 5 encoders and 5 decoders with fewer filters.
The code for creating the model.h5 file and predictions are also given.
The file feature-selection dataset contains the code for applying feature selection technqiue using the openCV library and generating the dataset of the feature selected images.

Dataset:
We used the publically available KITS 19 Challenge dataset. The dataset is available at this [link](https://github.com/neheller/kits19)

Usage:
a) In the images_to_PNGslices notebook, we visualized the data, converted the 3D images to PNG slices, and stored them in Google Drive.

b) training_unet_(1) notebook includes UNET model training on the generated png slices.

c) In dropout_0_05 notebook dropouts are added in the UNET model.

d) In classification_vgg16(1) notebook the experiment is performed where first the data is passed through a classifier and then the output from the classifier is further passed into UNET for segmentation.

e) dense-full(1) notebook includes the addition of dense layers within the UNET model.

Trained Model:
The trained model can be downloaded [here. ](https://drive.google.com/file/d/14RMZTk4B3iVD7PK55CiThARcWCqi489l/view?usp=sharing)

Web Application:
A Flask-based web application has also been developed to demonstrate the model and display the results. The source code can be found in the [Web_app](https://github.com/Manahil-shaikh/UNET-architecture-for-image-segmentation-of-Chronic-Kidney-disease-and-Feature-selection-techniques/tree/main/Web_App) folder.
