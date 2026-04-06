{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPdtiwQh1HHxyxHwY68jANZ",
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
        "<a href=\"https://colab.research.google.com/github/hiyalukka/ClassFlow/blob/main/tracker.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "XZu6D3253fGQ"
      },
      "outputs": [],
      "source": [
        "# python-progress-tracker\n",
        "# Phase 1 — Log and view study sessions\n",
        "# Built by: Hiya"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Simple Progress Tracker (No imports)\n",
        "\n",
        "while True:\n",
        "    print(\"\\n--- Progress Tracker ---\")\n",
        "    print(\"1. Add Study Session\")\n",
        "    print(\"2. View Progress\")\n",
        "    print(\"3. Exit\")\n",
        "\n",
        "    choice = input(\"Enter your choice: \")\n",
        "\n",
        "    if choice == \"1\":\n",
        "        date = input(\"Enter date (YYYY-MM-DD): \")\n",
        "        topic = input(\"What did you study today? \")\n",
        "        hours = input(\"How many hours did you study? \")\n",
        "\n",
        "        file = open(\"progress.txt\", \"a\")\n",
        "        file.write(date + \" | \" + topic + \" | \" + hours + \"\\n\")\n",
        "        file.close()\n",
        "\n",
        "        print(\"Progress saved!\")\n",
        "\n",
        "    elif choice == \"2\":\n",
        "        try:\n",
        "            file = open(\"progress.txt\", \"r\")\n",
        "            lines = file.readlines()\n",
        "            file.close()\n",
        "\n",
        "            total = 0\n",
        "\n",
        "            print(\"\\nYour Progress:\\n\")\n",
        "\n",
        "            for line in lines:\n",
        "                print(line.strip())\n",
        "\n",
        "                parts = line.split(\"|\")\n",
        "                h = float(parts[2])\n",
        "                total = total + h\n",
        "\n",
        "            print(\"\\nTotal Hours Studied:\", total)\n",
        "\n",
        "        except:\n",
        "            print(\"No progress found yet.\")\n",
        "\n",
        "    elif choice == \"3\":\n",
        "        print(\"Goodbye!\")\n",
        "        break\n",
        "\n",
        "    else:\n",
        "        print(\"Invalid choice\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "54mDLAeY3t6E",
        "outputId": "173a5828-f731-442f-b2ad-18b93f5892fb"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "--- Progress Tracker ---\n",
            "1. Add Study Session\n",
            "2. View Progress\n",
            "3. Exit\n",
            "Enter your choice: 1\n",
            "Enter date (YYYY-MM-DD): 06-04-2026\n",
            "What did you study today? python\n",
            "How many hours did you study? 1.5\n",
            "Progress saved!\n",
            "\n",
            "--- Progress Tracker ---\n",
            "1. Add Study Session\n",
            "2. View Progress\n",
            "3. Exit\n",
            "Enter your choice: 1\n",
            "Enter date (YYYY-MM-DD): 05-04-2026\n",
            "What did you study today? english\n",
            "How many hours did you study? 2\n",
            "Progress saved!\n",
            "\n",
            "--- Progress Tracker ---\n",
            "1. Add Study Session\n",
            "2. View Progress\n",
            "3. Exit\n",
            "Enter your choice: 2\n",
            "\n",
            "Your Progress:\n",
            "\n",
            "python - 1.5 hours\n",
            "No progress found yet.\n",
            "\n",
            "--- Progress Tracker ---\n",
            "1. Add Study Session\n",
            "2. View Progress\n",
            "3. Exit\n",
            "Enter your choice: 3\n",
            "Goodbye!\n"
          ]
        }
      ]
    }
  ]
}