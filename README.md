# lineartanimdata3

## Colab notebook

https://colab.research.google.com/drive/1Z2MeOLl7faqrdQcEUf0SYuR_10Z_Un1X#scrollTo=XmZpc-N_mEF9

## Local execution (only with GPU)

*NOTE: It's possible to run APISR without GPU but it's 20 times slower*

git clone https://github.com/rtous/lineartanimdata3
cd lineartanimdata3
python3.11 -m venv myvenv
source myvenv/bin/activate
cd APISR
pip install -r requirements.txt
pip install ffmpegcv
wget https://github.com/Kiteretsu77/APISR/releases/download/v0.1.0/2x_APISR_RRDB_GAN_generator.pth -P pretrained
python test_code/inference.py --model RRDB --scale 2 --input_dir ../data/scenes/test/imagesFull  --weight_path pretrained/2x_APISR_RRDB_GAN_generator.pth  --store_dir ../data/scenes/test/imagesFull_APISR

