{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/xyt100/HW1/blob/main/getBondPrice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def getBondPrice(y, face, couponRate, m, ppy=1):\n",
        "    N = m * ppy\n",
        "    cpn = couponRate * face / ppy\n",
        "    bondPrice = cpn * (1 - (1 + y/ppy) ** (-N)) / (y/ppy) + face * (1 + y/ppy) ** (-N)\n",
        "    return bondPrice"
      ],
      "metadata": {
        "id": "FBRasEBsmzs8"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SMC-bUUN9-gj",
        "outputId": "5a5f91ff-f9c8-4a99-840f-6fe21529c206"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2170604.056735517"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ],
      "source": [
        "#!/usr/bin/env python3\n",
        "# -*- coding: utf-8 -*-\n",
        "\"\"\"\n",
        "Created on Tue Jun 11 21:18:56 2024\n",
        "\n",
        "@author: tleitch\n",
        "\"\"\"\n",
        "\n",
        "def getBondPrice(y, face, couponRate, m, ppy=1):\n",
        "    df=1/(1+y/ppy)\n",
        "    bondPrice=0\n",
        "    cpn=couponRate*face/ppy\n",
        "\n",
        "    return(bondPrice)\n",
        "\n",
        "\n",
        "# Test values\n",
        "\n",
        "y = 0.03\n",
        "face = 2000000\n",
        "couponRate = 0.04\n",
        "m = 10\n",
        "ppy = 1\n",
        "ppy = 2\n",
        "#<no ppy value passed>\n",
        "\n",
        "getBondPrice(y, face, couponRate, m)"
      ]
    }
  ]
}