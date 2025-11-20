# lineartanimdata3


python3.11 -m venv myvenv
source myvenv/bin/activate
cd APISR
pip install -r requirements.txt
pip install ffmpegcv
wget https://github.com/Kiteretsu77/APISR/releases/download/v0.1.0/2x_APISR_RRDB_GAN_generator.pth -P pretrained
python test_code/inference.py --model RRDB --scale 2 --input_dir ../data/scenes/test/imagesFull  --weight_path pretrained/2x_APISR_RRDB_GAN_generator.pth  --store_dir ../data/scenes/test/imagesFull_APISR

## setup APISR (DISCARDED)

git clone https://github.com/Kiteretsu77/APISR.git
cd APISR
python3.11 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
pip install ffmpegcv
#wget https://github.com/Kiteretsu77/APISR/releases/download/v0.1.0/4x_APISR_GRL_GAN_generator.pth -P pretrained
wget https://github.com/Kiteretsu77/APISR/releases/download/v0.1.0/2x_APISR_RRDB_GAN_generator.pth -P pretrained
python test_code/inference.py --model RRDB --scale 2 --input_dir ../lineartanimdata3/data/scenes/test/imagesFull  --weight_path pretrained/2x_APISR_RRDB_GAN_generator.pth  --store_dir ../lineartanimdata3/data/scenes/test/imagesFull_APISR

