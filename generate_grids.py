# %%
import os
from PIL import Image
import matplotlib.pyplot as plt

# Path to the Datasets folder
base_dir = "Dataset"
base_dir

#%%
# Get the models (folders inside Dataset), with 'Real_painting' first
all_dirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
models = ['Real_painting'] + [d for d in all_dirs if d != 'Real_painting']

# Get all authors (assuming all models have the same authors)
first_model = models[0]
authors = sorted([d for d in os.listdir(os.path.join(base_dir, first_model)) if os.path.isdir(os.path.join(base_dir, first_model, d))])

# For each author, create a grid
for author in authors:
    fig, axes = plt.subplots(nrows=10, ncols=len(models), figsize=(2*len(models), 20))
    fig.suptitle(f'Author: {author}', fontsize=16)
    
    # Set model names as column titles
    for j, model in enumerate(models):
        axes[0, j].set_title(model, fontsize=12, pad=20)
    
    for i in range(10):  # For each image (0.png to 9.png)
        for j, model in enumerate(models):
            img_path = os.path.join(base_dir, model, author, f"{i}.png")
            ax = axes[i, j]
            ax.axis('off')
            if os.path.exists(img_path):
                img = Image.open(img_path)
                ax.imshow(img)
            else:
                ax.set_title('No image', fontsize=6)
    
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    grid_folder = "Grids"
    if not os.path.exists(grid_folder):
        os.makedirs(grid_folder)
    plt.savefig(f"{grid_folder}/grid_{author}.png")
    plt.close()


