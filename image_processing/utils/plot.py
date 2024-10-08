import matplotlib.pyplot as plt

def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplot(nrows=1, ncols = number_images, figsize=(12,4))  # type: ignore
    names_lst.append('Result') # type: ignore
    for ax, name, image in zip(axis, name_lst, args): # type: ignore
        ax.set_title(name)
        ax.inshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plot_histogram(image):
    fig, axis = plt.subpltos(nrows=1, ncols = 3, figsize=(12,4), sharex=True, sharey=True) # type: ignore
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color.title()))
        ax.hist(image[:,:, index].ravel(), bins = 256, color = color, alpha = 0.8)
    fig.tight_layout()
    plt.show()