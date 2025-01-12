{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMN30gwZNeS5nUO3rv9hMlM",
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
        "<a href=\"https://colab.research.google.com/github/Tarandeep0028/Cognitive-Computing-Assignment/blob/main/Assignment-1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Write a Python program to print \"Anything You find cool.\""
      ],
      "metadata": {
        "id": "iHQP2eTTRCx3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"hehe\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P_Y2G2MmRHtH",
        "outputId": "0915c333-6ca8-4d22-9018-3172bdadf822"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hehe\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q2 Add Numbers and Concatenate Strings  \n",
        "2.1 Write a program to add two numbers and print the result.                                  "
      ],
      "metadata": {
        "id": "ujbuhGWeRPo2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = 10\n",
        "b = 12\n",
        "a+b"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HHSKeoEtSwzc",
        "outputId": "27a600f1-3425-4ccb-b889-6bcb49d0efd2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "22"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.2 Write a program to concatenate two strings and print the result."
      ],
      "metadata": {
        "id": "DKI5c5end-bQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = \"Taran\"\n",
        "b = \"deep\"\n",
        "a+b"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "xDLVfrsIeDLb",
        "outputId": "0f04cd54-00c0-4783-b1f1-aeef853e9179"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Tarandeep'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.3 Write a program to concatenate a string and a number and print the result."
      ],
      "metadata": {
        "id": "2Ey0A22reOic"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = \"Tarandeep\"\n",
        "b = 028\n",
        "a+b"
      ],
      "metadata": {
        "id": "ANXAxxoreVT4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.1 Write a Python program to check if a number is positive, negative, or zero\n",
        "using an\n",
        "if-else statement."
      ],
      "metadata": {
        "id": "lQSytsmFhNqh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = 10\n",
        "if a>0:\n",
        "    print(\"positive\")\n",
        "elif a<0:\n",
        "    print(\"negative\")\n",
        "else:\n",
        "    print(\"zero\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XmV5pn3zhSUZ",
        "outputId": "4fa19afa-fe38-4951-efd2-8700bfb89fcf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "positive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.2 Write a program to check if a given number is odd or even."
      ],
      "metadata": {
        "id": "vQVnjAdnhu1-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = 12\n",
        "if a%2==0:\n",
        "    print(\"even\")\n",
        "else:\n",
        "    print(\"odd\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y0gtWpowhyGD",
        "outputId": "2b5a3215-5aa3-402e-9bd8-91e4291ac6c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "even\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " 4.1 Write a program to print numbers from 1 to 10 using a\n",
        "for loop."
      ],
      "metadata": {
        "id": "7F7mdKPfiFuE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,11):\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gH6xhe5eiKb-",
        "outputId": "a834a70f-b375-4672-c1e4-6491f37e66ea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4.2 Write a program to print numbers from 1 to 10 using a\n",
        "while loop."
      ],
      "metadata": {
        "id": "G9MrPCDLigJd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "i = 1\n",
        "while i in range(1,11):\n",
        "  print(i)\n",
        "  i = i+1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4uhG49b-ijXS",
        "outputId": "33f053a2-006f-4807-9206-9ee6c16aaf3b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4.3 Write a program to calculate the sum of numbers from 1 to 100 using a loop."
      ],
      "metadata": {
        "id": "TmpsMEqHjbHS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "total = 0\n",
        "for i in range(1,101):\n",
        "  total = total+i\n",
        "print(total)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "20a_zjc1jlvp",
        "outputId": "73ec6515-6b06-4043-bf83-84afd4388447"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5050\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " 5.1 Create a list of 5 numbers. Write a program to find the largest and smallest\n",
        "numbers in the list."
      ],
      "metadata": {
        "id": "NyBGdDUHkDhU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [1,2,3,4,5]\n",
        "max = max(numbers)\n",
        "min = min(numbers)\n",
        "print(max)\n",
        "print(min)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iUXOPLYzkHRu",
        "outputId": "774b3018-2ccc-4653-9cb6-a49fd9c4c21e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " 5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve\n",
        "the value of a given key."
      ],
      "metadata": {
        "id": "iyA3ycJvmQPm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dictionary = {1: 'key',2: 'value',3: 'pairs'}\n",
        "print(dictionary)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P8DCoA2XmURu",
        "outputId": "4c5676fc-a388-40a1-bc45-723b0c66f27f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1: 'key', 2: 'value', 3: 'pairs'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " 5.3 Write a program to sort a list of numbers in ascending and descending order."
      ],
      "metadata": {
        "id": "hxjbnizrqxUF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [5,7,3,6,2,4,1]\n",
        "numbers.sort()\n",
        "print(numbers)\n",
        "numbers.sort(reverse=True)\n",
        "print(numbers)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v0fnAbemq1r8",
        "outputId": "c7667c33-ccb7-4835-a739-adf9e780c465"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5, 6, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " 5.4 Write a program to merge two dictionaries into one."
      ],
      "metadata": {
        "id": "nw4UTSwqyelx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dictionary1 = {1: 'key',2: 'value',3: 'pairs'}\n",
        "dictionary2 = {4: 'key',5: 'value',6: 'pairs'}\n",
        "print(dictionary1|dictionary2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_XoDNUAMyfxm",
        "outputId": "d2f4c59e-086a-4fac-a6f0-583280ae1ca8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1: 'key', 2: 'value', 3: 'pairs', 4: 'key', 5: 'value', 6: 'pairs'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " 6.1 Write a program to count the number of vowels in a given string."
      ],
      "metadata": {
        "id": "u-r1tuJ7yjnW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "string = \"Tarandeep\"\n",
        "vowels = \"aeiouAEIOU\"\n",
        "count = 0\n",
        "for vowel in string:\n",
        "  if vowel in vowels:\n",
        "    count = count+1\n",
        "print(count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FqgoaU3Fyqsk",
        "outputId": "b0fd70db-e152-4ec3-f590-ea826fb6871a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6.2 Write a program to reverse a string and print it."
      ],
      "metadata": {
        "id": "DvyGzjco9AK_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "string = \"Tarandeep\"\n",
        "reverse = string[::-1]\n",
        "print(reverse)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X8-8ZHE49DVM",
        "outputId": "96d7d142-9645-4d63-bd96-a90134757ff5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "peednaraT\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " 6.3 Write a program to check if a string is a palindrome."
      ],
      "metadata": {
        "id": "YpBbzz7DCqk7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "string = \"level\"\n",
        "reverse = string[::-1]\n",
        "if string == reverse:\n",
        "  print(\"palindrome\")\n",
        "else:\n",
        "  print(\"not palindrome\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-WPpQ1l6CvoR",
        "outputId": "150b42bc-1b50-4a66-80a8-a75b4e468c1f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "palindrome\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "7.1 Write a program to create a text file, write some text into it, and then read and\n",
        "print the content."
      ],
      "metadata": {
        "id": "Wafkd5jVEG35"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "hEYtIVfIwrEw"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}