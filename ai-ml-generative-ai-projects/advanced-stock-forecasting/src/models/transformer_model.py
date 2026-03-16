import tensorflow as tf
from tensorflow.keras.layers import Dense, MultiHeadAttention, LayerNormalization
from tensorflow.keras.models import Model


class TransformerBlock(tf.keras.layers.Layer):

    def __init__(self, embed_dim, num_heads, ff_dim):

        super().__init__()

        self.att = MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)

        self.ffn = tf.keras.Sequential(
            [
                Dense(ff_dim, activation="relu"),
                Dense(embed_dim),
            ]
        )

        self.layernorm1 = LayerNormalization()
        self.layernorm2 = LayerNormalization()

    def call(self, inputs):

        attn_output = self.att(inputs, inputs)

        out1 = self.layernorm1(inputs + attn_output)

        ffn_output = self.ffn(out1)

        return self.layernorm2(out1 + ffn_output)


def build_transformer(input_shape):

    inputs = tf.keras.Input(shape=input_shape)

    x = TransformerBlock(64, 4, 128)(inputs)

    x = Dense(32, activation="relu")(x)

    outputs = Dense(1)(x)

    model = Model(inputs, outputs)

    model.compile(optimizer="adam", loss="mse")

    return model
