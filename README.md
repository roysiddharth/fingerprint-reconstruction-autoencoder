# Fingerprint Reconstruction App
Fingerprint Reconstruction model using Autoencoder (CNN) built with Tensorflow and Keras framework and deployed using Streamlit (and possibly Heroku in the near future).

# Author
[Siddhartha Roy](https://github.com/roysiddharth)

# Data
- [Training Data: Sokoto Coventry Fingerprint Dataset (SOCOFing)](https://www.kaggle.com/datasets/ruizgara/socofing)
- Testing Data is provided under the folder 'real-data'. You may use any other fingerprint image of your choice on the app as well.

# Dataset Description
> Sokoto Coventry Fingerprint Dataset (SOCOFing) is a biometric fingerprint database designed for academic research purposes. SOCOFing is made up of 6,000 fingerprint images from 600 African subjects and contains unique attributes such as labels for gender, hand and finger name as well as synthetically altered versions with three different levels of alteration for obliteration, central rotation, and z-cut. For a complete formal description and usage policy please refer to [this](https://arxiv.org/abs/1807.10609) paper.

# Libraries Used
- numpy
- tensorflow 2.9
- keras
- pickle
- glob
- PIL (for image manipulations)
- scikit-learn

# How to deploy using Streamlit and Google Colab
We had to use Streamlit on Google Colab because we wanted to utilize the processing power that Google so generously provides us through the GPUs.
### Steps
- Upload the files "app.py" and your choice of model.pickle file to the colab environment.
- Install Streamlit and Tensorflow quietly in the environment (if not already installed) using:
```
!pip install streamlit -q
!pip install tensorflow -q
```
- Once installation is finished, run:
`!streamlit run app.py & npx localtunnel --port 8501`
- You will be provided with an URL to run the app in a browser window. Click on it and you are ready to reconstruct your fingerprint of choice!

# References
- [Using Deep Learning to reconstruct fingerprints — With Keras](https://medium.com/analytics-vidhya/using-deep-learning-to-reconstruct-fingerprints-with-keras-daf44881b812)
- [Reconstructing Fingerprint Images Using Deep Learning (Convolutional Autoencoder)](https://www.datacamp.com/tutorial/fingerprint-deep-learning)
- [Recreating Fingerprints using Convolutional Autoencoders](https://www.kdnuggets.com/2020/03/recreating-fingerprints-using-convolutional-autoencoders.html)
- [Intuitively Understanding Convolutions for Deep Learning](https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1)
