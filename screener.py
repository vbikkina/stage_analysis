{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPLK+0+HVnPOIhdmwfGxnNo",
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
        "<a href=\"https://colab.research.google.com/github/vbikkina/stage_analysis/blob/test/screener.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nWClvxrQW5G3",
        "outputId": "5ccc873b-dc70-42e1-a675-52d8388b7624"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing BRK-B...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing MELI...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n",
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing IBKR...\n",
            "\n",
            "🔎 Analyzing AAPL...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing MSFT...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing NVDA...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing GOOGL...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n",
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing AMZN...\n",
            "\n",
            "🔎 Analyzing TSLA...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n",
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing ASTS...\n",
            "\n",
            "🔎 Analyzing HOOD...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing AMD...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing TSM...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n",
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing UPST...\n",
            "\n",
            "🔎 Analyzing NU...\n",
            "\n",
            "🔎 Analyzing TEM...\n",
            "\n",
            "🔎 Analyzing ADBE...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing ADYEY...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing ASML...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing CELH...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing CPRT...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing CRWD...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n",
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing DDOG...\n",
            "\n",
            "🔎 Analyzing DUOL...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing FRPH...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n",
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing HIMS...\n",
            "\n",
            "🔎 Analyzing MSTR...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n",
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing PAYC...\n",
            "\n",
            "🔎 Analyzing ROKU...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing TTD...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "🔎 Analyzing TXN...\n",
            "\n",
            "📊 Full Stock Report:\n",
            "\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| Ticker   |   Price |    50MA |   200MA |   %_Above_200MA |      MRS |   MRS_52MA |   Prev_High | High_Date   |   %_From_High | Buy                   |\n",
            "+==========+=========+=========+=========+=================+==========+============+=============+=============+===============+=======================+\n",
            "| BRK-B    |  503.96 |  470.88 |  363.7  |           38.56 |  -0.0168 |     0.0014 |      539.8  | 2025-04-28  |          6.64 |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| MELI     | 2563.29 | 1990.83 | 1434.72 |           78.66 |   0.0044 |     0.0061 |     2584.92 | 2025-05-12  |          0.84 |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| IBKR     |  209.68 |  164.97 |   99.96 |          109.76 |  -0.0013 |     0.009  |      233.47 | 2025-02-10  |         10.19 | 🚨 Overvalued         |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| AAPL     |  200.85 |  223.79 |  178.46 |           12.55 |   0.0108 |    -0.0009 |      254.97 | 2024-12-23  |         21.23 | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| MSFT     |  460.36 |  418.53 |  335.81 |           37.09 |   0.0049 |     0      |      464    | 2024-07-01  |          0.79 |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| NVDA     |  135.13 |  125.88 |   58.74 |          130.05 |   0.0115 |     0.0043 |      147.61 | 2024-11-04  |          8.45 | 🚨 Overvalued         |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| GOOGL    |  171.74 |  171.79 |  137.44 |           24.96 |   0.0017 |    -0.0019 |      203.79 | 2025-01-27  |         15.73 | 💡 Opportunity to Buy |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| AMZN     |  205.01 |  198.86 |  153.73 |           33.36 |   0.0022 |     0.0011 |      237.68 | 2025-01-27  |         13.75 |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| TSLA     |  346.46 |  292.35 |  252.19 |           37.38 |   0.0032 |     0.0142 |      436.23 | 2024-12-09  |         20.58 |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| ASTS     |   23.07 |   23.71 |   10.77 |          114.22 |  -0.0603 |     0.0253 |       33.4  | 2025-03-03  |         30.93 | 🚨 Overvalued         |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| HOOD     |   66.15 |   36.62 |   20.44 |          223.67 |   0.0294 |     0.0249 |       66.15 | 2025-05-26  |          0    | 🚨 Overvalued         |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| AMD      |  110.73 |  130.05 |  116.81 |           -5.21 |  -0.0139 |    -0.0082 |      207.39 | 2024-03-04  |         46.61 | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| TSM      |  193.32 |  182.85 |  119.91 |           61.22 |  -0.0108 |     0.0038 |      221.02 | 2025-01-20  |         12.53 |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| UPST     |   47.17 |   50.68 |   63.64 |          -25.88 |   0.0244 |     0.0201 |      390    | 2021-10-11  |         87.91 | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| NU       |  nan    |  nan    |  nan    |          nan    | nan      |   nan      |      nan    | nan         |        nan    | No Data               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| TEM      |  nan    |  nan    |  nan    |          nan    | nan      |   nan      |      nan    | nan         |        nan    | No Data               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| ADBE     |  415.09 |  471.27 |  474.03 |          -12.43 |   0.0004 |    -0.0029 |      688.37 | 2021-11-15  |         39.7  | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| ADYEY    |   19.15 |   15.13 |   16.46 |           16.37 |   0.0461 |     0.0067 |       32.3  | 2021-08-23  |         40.71 |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| ASML     |  736.77 |  768.06 |  699.29 |            5.36 |  -0.0119 |    -0.006  |     1077.9  | 2024-07-08  |         31.65 | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| CELH     |   37.88 |   34.76 |   38.91 |           -2.64 |   0.0316 |    -0.0117 |       95.15 | 2024-05-20  |         60.19 |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| CPRT     |   51.48 |   55.69 |   42.99 |           19.75 |  -0.0586 |    -0.0024 |       63.84 | 2025-05-12  |         19.36 | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| CRWD     |  471.37 |  348.82 |  237.55 |           98.43 |   0.0169 |     0.0084 |      471.37 | 2025-05-26  |          0    |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| DDOG     |  117.88 |  122.73 |  114.51 |            2.94 |   0.0121 |     0.0005 |      193.03 | 2021-11-08  |         38.93 | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| DUOL     |  519.61 |  311.95 |  179.38 |          189.67 |  -0.0189 |     0.02   |      529.05 | 2025-05-12  |          1.78 | 🚨 Overvalued         |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| FRPH     |   27.12 |   29.35 |   29.03 |           -6.58 |   0.0068 |    -0.0045 |       32.5  | 2021-11-01  |         16.55 | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| HIMS     |   56.56 |   28.89 |   13.17 |          329.4  |   0.0138 |     0.0287 |       64.65 | 2025-05-12  |         12.51 | 🚨 Overvalued         |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| MSTR     |  369.06 |  270.92 |  105.75 |          248.99 |  -0.019  |     0.0204 |      421.88 | 2024-11-18  |         12.52 | 🚨 Overvalued         |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| PAYC     |  259.09 |  196.98 |  275.94 |           -6.11 |  -0.0117 |     0.0101 |      539.08 | 2021-10-25  |         51.94 |                       |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| ROKU     |   72.46 |   71.13 |  100.31 |          -27.77 |   0.0322 |     0.0056 |      473.65 | 2021-07-19  |         84.7  | ⚠️ Caution            |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| TTD      |   75.22 |   96.7  |   76.17 |           -1.25 |   0.0002 |    -0.0029 |      139.11 | 2024-12-02  |         45.93 | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n",
            "| TXN      |  182.85 |  187.44 |  167.68 |            9.04 |   0.0194 |    -0.0023 |      216.82 | 2024-11-04  |         15.67 | ❌ Sell               |\n",
            "+----------+---------+---------+---------+-----------------+----------+------------+-------------+-------------+---------------+-----------------------+\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-1-824416999086>:36: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_close = float(last['Close'])\n",
            "<ipython-input-1-824416999086>:37: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_50 = float(last['50MA'])\n",
            "<ipython-input-1-824416999086>:38: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_200 = float(last['200MA'])\n",
            "<ipython-input-1-824416999086>:39: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs = float(last['Mansfield_RS'])\n",
            "<ipython-input-1-824416999086>:40: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  last_rs_ma = float(last['MRS_52MA'])\n",
            "<ipython-input-1-824416999086>:43: FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead\n",
            "  high_price = float(combined['Close'].max())\n"
          ]
        }
      ],
      "source": [
        "import yfinance as yf\n",
        "import pandas as pd\n",
        "from tabulate import tabulate\n",
        "\n",
        "def get_spy_benchmark(period='5y', interval='1wk'):\n",
        "    \"\"\"Download SPY benchmark for Mansfield RS calculations.\"\"\"\n",
        "    spy = yf.download('SPY', period=period, interval=interval, auto_adjust=True, progress=False)\n",
        "    spy['SPY_Return'] = spy['Close'].pct_change()\n",
        "    return spy[['SPY_Return']]\n",
        "\n",
        "def analyze_stock(\n",
        "    ticker,\n",
        "    spy_benchmark,\n",
        "    period='5y',\n",
        "    interval='1wk',\n",
        "    min_data_points=200\n",
        "):\n",
        "    \"\"\"Analyze a single stock and compute signals.\"\"\"\n",
        "    try:\n",
        "        df = yf.download(ticker, period=period, interval=interval, auto_adjust=True, progress=False)\n",
        "        if df.empty or 'Close' not in df.columns:\n",
        "            return {'Ticker': ticker, 'Buy': 'No Data'}\n",
        "\n",
        "        df['50MA'] = df['Close'].rolling(window=50).mean()\n",
        "        df['200MA'] = df['Close'].rolling(window=200).mean()\n",
        "        df['Stock_Return'] = df['Close'].pct_change()\n",
        "\n",
        "        combined = df.join(spy_benchmark, how='inner')\n",
        "        combined['Mansfield_RS'] = combined['Stock_Return'] - combined['SPY_Return']\n",
        "        combined['MRS_52MA'] = combined['Mansfield_RS'].rolling(window=52).mean()\n",
        "\n",
        "        if len(combined) < min_data_points:\n",
        "            return {'Ticker': ticker, 'Buy': 'No Data'}\n",
        "\n",
        "        last = combined.iloc[-1]\n",
        "        last_close = float(last['Close'])\n",
        "        last_50 = float(last['50MA'])\n",
        "        last_200 = float(last['200MA'])\n",
        "        last_rs = float(last['Mansfield_RS'])\n",
        "        last_rs_ma = float(last['MRS_52MA'])\n",
        "\n",
        "        above_200_pct = round((last_close - last_200) / last_200 * 100, 2)\n",
        "        high_price = float(combined['Close'].max())\n",
        "        high_date = combined['Close'].idxmax()\n",
        "        if isinstance(high_date, pd.Series):\n",
        "            high_date = high_date.iloc[0]\n",
        "        high_date = high_date.strftime('%Y-%m-%d')\n",
        "        percent_from_high = round(100 * (high_price - last_close) / high_price, 2)\n",
        "        if last_close > high_price:\n",
        "            percent_from_high = -abs(percent_from_high)\n",
        "\n",
        "        # Buy criteria\n",
        "        # Guard for NaN in moving average\n",
        "        if combined['50MA'].isnull().sum() > 0:\n",
        "            ma_rising = False\n",
        "        else:\n",
        "            ma_rising = combined['50MA'].iloc[-3] < combined['50MA'].iloc[-2] < combined['50MA'].iloc[-1]\n",
        "        above_200 = last_50 > last_200\n",
        "        above_50 = last_close > last_50\n",
        "        strong_rs = last_rs > last_rs_ma\n",
        "\n",
        "        # Buy signal logic (refined order)\n",
        "        buy_signal = ''\n",
        "        if above_200_pct > 100:\n",
        "            buy_signal = '🚨 Overvalued'\n",
        "        elif abs(last_close - last_50) / last_50 <= 0.005:\n",
        "            buy_signal = '💡 Opportunity to Buy'\n",
        "        elif all([ma_rising, above_200, above_50, strong_rs]):\n",
        "            buy_signal = '✅ Buy'\n",
        "        elif abs(last_close - last_50) / last_50 <= 0.02:\n",
        "            buy_signal = '⚠️ Caution'\n",
        "        elif last_close < last_50:\n",
        "            buy_signal = '❌ Sell'\n",
        "\n",
        "        return {\n",
        "            'Ticker': ticker,\n",
        "            'Price': round(last_close, 2),\n",
        "            '50MA': round(last_50, 2),\n",
        "            '200MA': round(last_200, 2),\n",
        "            '%_Above_200MA': above_200_pct,\n",
        "            'MRS': round(last_rs, 4),\n",
        "            'MRS_52MA': round(last_rs_ma, 4),\n",
        "            'Prev_High': round(high_price, 2),\n",
        "            'High_Date': high_date,\n",
        "            '%_From_High': percent_from_high,\n",
        "            'Buy': buy_signal\n",
        "        }\n",
        "    except Exception as e:\n",
        "        print(f\"❌ Error processing {ticker}: {e}\")\n",
        "        return {'Ticker': ticker, 'Buy': 'No Data'}\n",
        "\n",
        "def analyze_stocks(\n",
        "    stock_list,\n",
        "    period='5y',\n",
        "    interval='1wk',\n",
        "    min_data_points=200,\n",
        "    verbose=True\n",
        "):\n",
        "    \"\"\"Analyze a list of stocks and return a DataFrame with results.\"\"\"\n",
        "    spy_benchmark = get_spy_benchmark(period=period, interval=interval)\n",
        "    all_results = []\n",
        "    for symbol in stock_list:\n",
        "        if verbose:\n",
        "            print(f\"\\n🔎 Analyzing {symbol}...\")\n",
        "        result = analyze_stock(\n",
        "            symbol,\n",
        "            spy_benchmark,\n",
        "            period=period,\n",
        "            interval=interval,\n",
        "            min_data_points=min_data_points\n",
        "        )\n",
        "        if result:\n",
        "            all_results.append(result)\n",
        "    df = pd.DataFrame(all_results)\n",
        "    return df\n",
        "\n",
        "def print_report(df):\n",
        "    \"\"\"Print the stock analysis report in a tabular format.\"\"\"\n",
        "    if df.empty:\n",
        "        print(\"\\n❌ No data available.\")\n",
        "    else:\n",
        "        print(\"\\n📊 Full Stock Report:\\n\")\n",
        "        print(tabulate(df, headers=\"keys\", tablefmt=\"grid\", showindex=False))\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    # Example usage\n",
        "    stock_list = [\n",
        "        'BRK-B','MELI','IBKR','AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'TSLA',\n",
        "        'ASTS', 'HOOD', 'AMD', 'TSM', 'UPST', 'NU', 'TEM',\n",
        "        'ADBE', 'ADYEY', 'ASML', 'CELH', 'CPRT', 'CRWD', 'DDOG', 'DUOL', 'FRPH',\n",
        "        'HIMS', 'MSTR', 'PAYC', 'ROKU', 'TTD', 'TXN'\n",
        "    ]\n",
        "    df = analyze_stocks(stock_list)\n",
        "    print_report(df)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "FVA9xxSxXmEu"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}