## Setting up environment
- Set up a Python 3.12.8 environment. Python 3.12.8 [Miniconda Distribution](https://www.anaconda.com/download)
- Install the required packages by using pip and the provided requirements.txt file
- Install Pytorch with Cuda 12.6 using the following command:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```
- In case, there are problems with installing or running Pytorch then check their [instructions](https://pytorch.org/get-started/locally/).

### Files:
- Dataset_Preprocessing.ipynb: Loads the datasets and changes it format to YOLO format suitable for training withour code
- Main_KITTI.ipynb: Changing model layers, training
- Results_KITTI.ipynb: Get predictions, convert them to orignal format, check mAP, plot some examples
### Reproducing results
- Setup environment
- Download YOLOV3 MSCOCO checkpoint on image size 608 from [link](https://data.pjreddie.com/files/yolov3.weights)
- Paste the weights file in project root directory as yolov3.weights
- Run the script model_with_weights2.py. This will produce a new file YOLOV3_MSCOCO_Orignal.pth.tar in project root
- Now the model part is ready

- Create a dir "KITTI" in the project root. Paste the given dataset numpy files inside it.
- Run the Dataset_Preprocessing.ipynb. This will create a new dir "KITTI_YOLO" with new dataset formats
- Run Main_KITTI.ipynb for training the model
- Run Results_KITTI.ipynb for getting predictions, mAP, plots

## Acknowledgements
This repository uses code adapted from the [Pytorch implementation of YOLOV3](https://github.com/SannaPersson/YOLOv3-PyTorch) by Aladin and Sana Persson 

Yolov3 is an object detector based on the following research paper:
@article{yolov3,
  title={YOLOv3: An Incremental Improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal = {arXiv},
  year={2018}
}