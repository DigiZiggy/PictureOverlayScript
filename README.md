**Project title**

Program to tint coloured 24bit photos with flag overlay.

**Project description**

Probably all of us have seen this kind of photos:
http://flagmypicture.com/img/profile_pictures/italian-flag-overlay.jpg

Task: Make Python3 program to tint photos like flag overlay.
You may use Estonian flag or flag of some other (your own) country. Stripes may be horisontal or vertical, minimum 3 stripe.
Program must work with different size of .jpg or .png photos (your own choice).

Additional Information:
Python 3 code.
Python 2 is not necessary. Tests and UI are not necessary.

Add documentation and comments.

**Screenshots**

![Alt text](Screenshot 2019-04-29 at 18.49.08.png?raw=true "Optional Title")



**Code Example**

Load photo from a file.
```angular2
filename = os.path.join(skimage.data_dir, 'smile.jpg')
smile_photo = io.imread(filename)
```

Read the image into numpy array
```angular2
image = img_as_float(smile_photo)
```

Slice the photo horizontally into 3 equals
```angular2
top_of_img, centre_of_img, bottom_of_img = slice_img_horizontally(image)
```

Make copy for each new flag from the original
```
estonian_image = image.copy()
```

Colorize the copied image with according method:
colorize_estonian_flag for coloring a copy of the photo in the colours of estonian flag
```angular2
colorize_estonian_flag(estonian_image, top_of_img, centre_of_img, bottom_of_img)
```

Set up the display area
```angular2
fig, ax = plt.subplots(ncols=2, nrows=4, figsize=(16, 12), sharex=True, sharey=True)
ax[0, 0].imshow(masked_image)
```

Show finished result on the previously set up display area
```
plt.show()
```


**How to use?**

Go into the Picture_overlay folder
```angular2
cd Picture_overlay
```

Make sure Scikit-image library is installed
```angular2
pip install scikit-image
```

Run the image overlay generator
```angular2
python3 overlay.py
```


**Credits**

Method colorize gotten from SciKit-image page

https://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_tinting_grayscale_images.html#sphx-glr-auto-examples-color-exposure-plot-tinting-grayscale-images-py

**License**

MIT © Sigrid Närep