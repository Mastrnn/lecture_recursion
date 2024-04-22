import matplotlib.pyplot as plt


def floodfill(image, x, y):
    if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
        return image

    if image[x][y] == 0 or image[x][y] == 2:
        return image

    image[x][y]=2

    plt.imshow(image)
    plt.pause(0.05)
    plt.clf()

    floodfill(image, x + 1, y)
    floodfill(image, x - 1, y)
    floodfill(image, x, y + 1)
    floodfill(image, x, y - 1)

    return image


def main():
    #img = plt.imread("files/img0.png")[:, :, 0]
    #img = plt.imread("files/img1.png")[:, :, 0]
    img = plt.imread("files/img2.png")[:, :, 0]

    img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()



if __name__ == "__main__":
    main()
