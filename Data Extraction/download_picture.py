from sklearn.cluster import KMeans
import numpy as np
import urllib.request
import cv2 #for resizing image

def read_url():
    train_photo = []
    with open('ML challenge photo 100.csv', 'r') as f:
        for line in f:
            train_photo.append(line.strip())
    return train_photo

def centorid_histogram(clt):

    numLabels = np.arange(0, len(np.unique(clt.labels_))+1)
    (hist, _) = np.histogram(clt.labels_, bins= numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def RGB_list(train_photo):
    imgRGB_list = []
    for photo in train_photo:
        resp = urllib.request.urlopen(photo)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        imgRGB_list.append([find_RGB(image)])
    return imgRGB_list

def find_RGB(image):
    #image = cv2.imread('red.jpg')
    # image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2RGB)
    h, w, _ = image.shape
    w_new = int(100 * w / max(w, h))
    h_new = int(100 * h / max(w, h))
    image = cv2.resize(image, (w_new, h_new))

    image_array = image.reshape((image.shape[0] * image.shape[1], 3))

    clt = KMeans(n_clusters=3)
    clt.fit(image_array)

    hist = centorid_histogram(clt)

    return hist



def main():
    url = read_url()
    imgRGB_list = RGB_list(url)
    print(imgRGB_list)


if __name__ == '__main__':
    main()
