#!/bin/bash

python train.py   --cell_type 'lstm' \
                  --attention_type 'luong' \
                  --hidden_units 200 \
                  --depth 2 \
                  --embedding_size 100 \
                  --num_encoder_symbols 128 \
                  --num_decoder_symbols 60 \
                  --save_freq 10000 \
                  --valid_freq 100