from src.model import AutoSeg
from src.model import sequence_contrastive_loss
from src.test_dataset import PascalVOCDataset, collate_fn_factory
from torch.utils.data import DataLoader
from transformers import CLIPProcessor, CLIPModel
from torch.optim import Adam
from torch import nn
import tqdm


# Define dataset dir
# change to the path of the VOC2012 dataset
dataset_dir = "../datasets/VOC2012/VOCdevkit/VOC2012/"
image_dir = "JPEGImages/"
label_file_path = "src/test_labels.txt"
data_file_path = "ImageSets/Segmentation/val.txt"
annotation_dir = "SegmentationClass/"


# Create dataset object
data = PascalVOCDataset(
    dataset_dir + image_dir,
    dataset_dir + annotation_dir,
    label_file_path,
    dataset_dir + data_file_path,
)

processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

collate_fn = collate_fn_factory(processor)

data_loader = DataLoader(data, batch_size=32, collate_fn=collate_fn, num_workers=2)

for batch in tqdm.tqdm(data_loader):
    print(batch)
