from contextlib import nullcontext


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": True
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['.git', '.ipynb_checkpoints', 'dataset', 'main.ipynb', 'test acc.png', 'test time.png', 'test_accuracy_figure.png', 'test_time_figure.png', 'train acc.png', 'train time.png', 'training_accuracy_figure.png', 'train_time_figure.png']\n"
     ]
    }
   ],
   "source": [
    "print(os.listdir('C:\\\\Users\\\\admin\\\\OneDrive\\\\Desktop\\\\Intrusion Detection System'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "back,buffer_overflow,ftp_write,guess_passwd,imap,ipsweep,land,loadmodule,multihop,neptune,nmap,normal,perl,phf,pod,portsweep,rootkit,satan,smurf,spy,teardrop,warezclient,warezmaster.\n",
      "duration: continuous.\n",
      "protocol_type: symbolic.\n",
      "service: symbolic.\n",
      "flag: symbolic.\n",
      "src_bytes: continuous.\n",
      "dst_bytes: continuous.\n",
      "land: symbolic.\n",
      "wrong_fragment: continuous.\n",
      "urgent: continuous.\n",
      "hot: continuous.\n",
      "num_failed_logins: continuous.\n",
      "logged_in: symbolic.\n",
      "num_compromised: continuous.\n",
      "root_shell: continuous.\n",
      "su_attempted: continuous.\n",
      "num_root: continuous.\n",
      "num_file_creations: continuous.\n",
      "num_shells: continuous.\n",
      "num_access_files: continuous.\n",
      "num_outbound_cmds: continuous.\n",
      "is_host_login: symbolic.\n",
      "is_guest_login: symbolic.\n",
      "count: continuous.\n",
      "srv_count: continuous.\n",
      "serror_rate: continuous.\n",
      "srv_serror_rate: continuous.\n",
      "rerror_rate: continuous.\n",
      "srv_rerror_rate: continuous.\n",
      "same_srv_rate: continuous.\n",
      "diff_srv_rate: continuous.\n",
      "srv_diff_host_rate: continuous.\n",
      "dst_host_count: continuous.\n",
      "dst_host_srv_count: continuous.\n",
      "dst_host_same_srv_rate: continuous.\n",
      "dst_host_diff_srv_rate: continuous.\n",
      "dst_host_same_src_port_rate: continuous.\n",
      "dst_host_srv_diff_host_rate: continuous.\n",
      "dst_host_serror_rate: continuous.\n",
      "dst_host_srv_serror_rate: continuous.\n",
      "dst_host_rerror_rate: continuous.\n",
      "dst_host_srv_rerror_rate: continuous.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open(\"C:\\\\Users\\\\admin\\\\OneDrive\\\\Desktop\\\\Intrusion Detection System\\\\dataset\\\\kddcup.names\",'r') as f:\n",
    "    print(f.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "42\n"
     ]
    }
   ],
   "source": [
    "cols=\"\"\"duration,\n",
    "protocol_type,\n",
    "service,\n",
    "flag,\n",
    "src_bytes,\n",
    "dst_bytes,\n",
    "land,\n",
    "wrong_fragment,\n",
    "urgent,\n",
    "hot,\n",
    "num_failed_logins,\n",
    "logged_in,\n",
    "num_compromised,\n",
    "root_shell,\n",
    "su_attempted,\n",
    "num_root,\n",
    "num_file_creations,\n",
    "num_shells,\n",
    "num_access_files,\n",
    "num_outbound_cmds,\n",
    "is_host_login,\n",
    "is_guest_login,\n",
    "count,\n",
    "srv_count,\n",
    "serror_rate,\n",
    "srv_serror_rate,\n",
    "rerror_rate,\n",
    "srv_rerror_rate,\n",
    "same_srv_rate,\n",
    "diff_srv_rate,\n",
    "srv_diff_host_rate,\n",
    "dst_host_count,\n",
    "dst_host_srv_count,\n",
    "dst_host_same_srv_rate,\n",
    "dst_host_diff_srv_rate,\n",
    "dst_host_same_src_port_rate,\n",
    "dst_host_srv_diff_host_rate,\n",
    "dst_host_serror_rate,\n",
    "dst_host_srv_serror_rate,\n",
    "dst_host_rerror_rate,\n",
    "dst_host_srv_rerror_rate\"\"\"\n",
    "\n",
    "columns=[]\n",
    "for c in cols.split(','):\n",
    "    if(c.strip()):\n",
    "       columns.append(c.strip())\n",
    "\n",
    "columns.append('target')\n",
    "#print(columns)\n",
    "print(len(columns))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "back dos\n",
      "buffer_overflow u2r\n",
      "ftp_write r2l\n",
      "guess_passwd r2l\n",
      "imap r2l\n",
      "ipsweep probe\n",
      "land dos\n",
      "loadmodule u2r\n",
      "multihop r2l\n",
      "neptune dos\n",
      "nmap probe\n",
      "perl u2r\n",
      "phf r2l\n",
      "pod dos\n",
      "portsweep probe\n",
      "rootkit u2r\n",
      "satan probe\n",
      "smurf dos\n",
      "spy r2l\n",
      "teardrop dos\n",
      "warezclient r2l\n",
      "warezmaster r2l\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open(\"C:\\\\Users\\\\admin\\\\OneDrive\\\\Desktop\\\\Intrusion Detection System\\\\dataset\\\\training_attack_types\",'r') as f:\n",
    "    print(f.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "attacks_types = {\n",
    "    'normal': 'normal',\n",
    "'back': 'dos',\n",
    "'buffer_overflow': 'u2r',\n",
    "'ftp_write': 'r2l',\n",
    "'guess_passwd': 'r2l',\n",
    "'imap': 'r2l',\n",
    "'ipsweep': 'probe',\n",
    "'land': 'dos',\n",
    "'loadmodule': 'u2r',\n",
    "'multihop': 'r2l',\n",
    "'neptune': 'dos',\n",
    "'nmap': 'probe',\n",
    "'perl': 'u2r',\n",
    "'phf': 'r2l',\n",
    "'pod': 'dos',\n",
    "'portsweep': 'probe',\n",
    "'rootkit': 'u2r',\n",
    "'satan': 'probe',\n",
    "'smurf': 'dos',\n",
    "'spy': 'r2l',\n",
    "'teardrop': 'dos',\n",
    "'warezclient': 'r2l',\n",
    "'warezmaster': 'r2l',\n",
    "}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "READING DATASET"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>duration</th>\n",
       "      <th>protocol_type</th>\n",
       "      <th>service</th>\n",
       "      <th>flag</th>\n",
       "      <th>src_bytes</th>\n",
       "      <th>dst_bytes</th>\n",
       "      <th>land</th>\n",
       "      <th>wrong_fragment</th>\n",
       "      <th>urgent</th>\n",
       "      <th>hot</th>\n",
       "      <th>...</th>\n",
       "      <th>dst_host_same_srv_rate</th>\n",
       "      <th>dst_host_diff_srv_rate</th>\n",
       "      <th>dst_host_same_src_port_rate</th>\n",
       "      <th>dst_host_srv_diff_host_rate</th>\n",
       "      <th>dst_host_serror_rate</th>\n",
       "      <th>dst_host_srv_serror_rate</th>\n",
       "      <th>dst_host_rerror_rate</th>\n",
       "      <th>dst_host_srv_rerror_rate</th>\n",
       "      <th>target</th>\n",
       "      <th>Attack Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>181</td>\n",
       "      <td>5450</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.11</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>239</td>\n",
       "      <td>486</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.05</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>235</td>\n",
       "      <td>1337</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>219</td>\n",
       "      <td>1337</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>217</td>\n",
       "      <td>2032</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.02</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 43 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   duration protocol_type service flag  src_bytes  dst_bytes  land  \\\n",
       "0         0           tcp    http   SF        181       5450     0   \n",
       "1         0           tcp    http   SF        239        486     0   \n",
       "2         0           tcp    http   SF        235       1337     0   \n",
       "3         0           tcp    http   SF        219       1337     0   \n",
       "4         0           tcp    http   SF        217       2032     0   \n",
       "\n",
       "   wrong_fragment  urgent  hot  ...  dst_host_same_srv_rate  \\\n",
       "0               0       0    0  ...                     1.0   \n",
       "1               0       0    0  ...                     1.0   \n",
       "2               0       0    0  ...                     1.0   \n",
       "3               0       0    0  ...                     1.0   \n",
       "4               0       0    0  ...                     1.0   \n",
       "\n",
       "   dst_host_diff_srv_rate  dst_host_same_src_port_rate  \\\n",
       "0                     0.0                         0.11   \n",
       "1                     0.0                         0.05   \n",
       "2                     0.0                         0.03   \n",
       "3                     0.0                         0.03   \n",
       "4                     0.0                         0.02   \n",
       "\n",
       "   dst_host_srv_diff_host_rate  dst_host_serror_rate  \\\n",
       "0                          0.0                   0.0   \n",
       "1                          0.0                   0.0   \n",
       "2                          0.0                   0.0   \n",
       "3                          0.0                   0.0   \n",
       "4                          0.0                   0.0   \n",
       "\n",
       "   dst_host_srv_serror_rate  dst_host_rerror_rate  dst_host_srv_rerror_rate  \\\n",
       "0                       0.0                   0.0                       0.0   \n",
       "1                       0.0                   0.0                       0.0   \n",
       "2                       0.0                   0.0                       0.0   \n",
       "3                       0.0                   0.0                       0.0   \n",
       "4                       0.0                   0.0                       0.0   \n",
       "\n",
       "    target  Attack Type  \n",
       "0  normal.       normal  \n",
       "1  normal.       normal  \n",
       "2  normal.       normal  \n",
       "3  normal.       normal  \n",
       "4  normal.       normal  \n",
       "\n",
       "[5 rows x 43 columns]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "path = \"C:\\\\Users\\\\admin\\\\OneDrive\\\\Desktop\\\\Intrusion Detection System\\\\dataset\\\\kddcup.data_10_percent.gz\"\n",
    "df = pd.read_csv(path,names=columns)\n",
    "\n",
    "#Adding Attack Type column\n",
    "df['Attack Type'] = df.target.apply(lambda r:attacks_types[r[:-1]])\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(494021, 43)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": False
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "smurf.              280790\n",
       "neptune.            107201\n",
       "normal.              97278\n",
       "back.                 2203\n",
       "satan.                1589\n",
       "ipsweep.              1247\n",
       "portsweep.            1040\n",
       "warezclient.          1020\n",
       "teardrop.              979\n",
       "pod.                   264\n",
       "nmap.                  231\n",
       "guess_passwd.           53\n",
       "buffer_overflow.        30\n",
       "land.                   21\n",
       "warezmaster.            20\n",
       "imap.                   12\n",
       "rootkit.                10\n",
       "loadmodule.              9\n",
       "ftp_write.               8\n",
       "multihop.                7\n",
       "phf.                     4\n",
       "perl.                    3\n",
       "spy.                     2\n",
       "Name: target, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['target'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dos       391458\n",
       "normal     97278\n",
       "probe       4107\n",
       "r2l         1126\n",
       "u2r           52\n",
       "Name: Attack Type, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Attack Type'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "duration                         int64\n",
       "protocol_type                   object\n",
       "service                         object\n",
       "flag                            object\n",
       "src_bytes                        int64\n",
       "dst_bytes                        int64\n",
       "land                             int64\n",
       "wrong_fragment                   int64\n",
       "urgent                           int64\n",
       "hot                              int64\n",
       "num_failed_logins                int64\n",
       "logged_in                        int64\n",
       "num_compromised                  int64\n",
       "root_shell                       int64\n",
       "su_attempted                     int64\n",
       "num_root                         int64\n",
       "num_file_creations               int64\n",
       "num_shells                       int64\n",
       "num_access_files                 int64\n",
       "num_outbound_cmds                int64\n",
       "is_host_login                    int64\n",
       "is_guest_login                   int64\n",
       "count                            int64\n",
       "srv_count                        int64\n",
       "serror_rate                    float64\n",
       "srv_serror_rate                float64\n",
       "rerror_rate                    float64\n",
       "srv_rerror_rate                float64\n",
       "same_srv_rate                  float64\n",
       "diff_srv_rate                  float64\n",
       "srv_diff_host_rate             float64\n",
       "dst_host_count                   int64\n",
       "dst_host_srv_count               int64\n",
       "dst_host_same_srv_rate         float64\n",
       "dst_host_diff_srv_rate         float64\n",
       "dst_host_same_src_port_rate    float64\n",
       "dst_host_srv_diff_host_rate    float64\n",
       "dst_host_serror_rate           float64\n",
       "dst_host_srv_serror_rate       float64\n",
       "dst_host_rerror_rate           float64\n",
       "dst_host_srv_rerror_rate       float64\n",
       "target                          object\n",
       "Attack Type                     object\n",
       "dtype: object"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "DATA PREPROCESSING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "duration                       0\n",
       "protocol_type                  0\n",
       "service                        0\n",
       "flag                           0\n",
       "src_bytes                      0\n",
       "dst_bytes                      0\n",
       "land                           0\n",
       "wrong_fragment                 0\n",
       "urgent                         0\n",
       "hot                            0\n",
       "num_failed_logins              0\n",
       "logged_in                      0\n",
       "num_compromised                0\n",
       "root_shell                     0\n",
       "su_attempted                   0\n",
       "num_root                       0\n",
       "num_file_creations             0\n",
       "num_shells                     0\n",
       "num_access_files               0\n",
       "num_outbound_cmds              0\n",
       "is_host_login                  0\n",
       "is_guest_login                 0\n",
       "count                          0\n",
       "srv_count                      0\n",
       "serror_rate                    0\n",
       "srv_serror_rate                0\n",
       "rerror_rate                    0\n",
       "srv_rerror_rate                0\n",
       "same_srv_rate                  0\n",
       "diff_srv_rate                  0\n",
       "srv_diff_host_rate             0\n",
       "dst_host_count                 0\n",
       "dst_host_srv_count             0\n",
       "dst_host_same_srv_rate         0\n",
       "dst_host_diff_srv_rate         0\n",
       "dst_host_same_src_port_rate    0\n",
       "dst_host_srv_diff_host_rate    0\n",
       "dst_host_serror_rate           0\n",
       "dst_host_srv_serror_rate       0\n",
       "dst_host_rerror_rate           0\n",
       "dst_host_srv_rerror_rate       0\n",
       "target                         0\n",
       "Attack Type                    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['flag', 'service', 'protocol_type']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Finding categorical features\n",
    "num_cols = df._get_numeric_data().columns\n",
    "\n",
    "cate_cols = list(set(df.columns)-set(num_cols))\n",
    "cate_cols.remove('target')\n",
    "cate_cols.remove('Attack Type')\n",
    "\n",
    "cate_cols"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CATEGORICAL FEATURES DISTRIBUTION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visualization\n",
    "def bar_graph(feature):\n",
    "    df[feature].value_counts().plot(kind=\"bar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "bar_graph('protocol_type')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Protocol type: We notice that ICMP is the most present in the used data, then TCP and almost 20000 packets of UDP type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,3))\n",
    "bar_graph('service')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "bar_graph('flag')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "bar_graph('logged_in')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "logged_in (1 if successfully logged in; 0 otherwise): We notice that just 70000 packets are successfully logged in."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "TARGET FEATURE DISTRIBUTION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "bar_graph('target')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Attack Type(The attack types grouped by attack, it's what we will predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "bar_graph('Attack Type')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['duration', 'protocol_type', 'service', 'flag', 'src_bytes',\n",
       "       'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',\n",
       "       'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',\n",
       "       'su_attempted', 'num_root', 'num_file_creations', 'num_shells',\n",
       "       'num_access_files', 'num_outbound_cmds', 'is_host_login',\n",
       "       'is_guest_login', 'count', 'srv_count', 'serror_rate',\n",
       "       'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',\n",
       "       'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',\n",
       "       'dst_host_srv_count', 'dst_host_same_srv_rate',\n",
       "       'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',\n",
       "       'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',\n",
       "       'dst_host_srv_serror_rate', 'dst_host_rerror_rate',\n",
       "       'dst_host_srv_rerror_rate', 'target', 'Attack Type'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "DATA CORRELATION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x864 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = df.dropna('columns')# drop columns with NaN\n",
    "\n",
    "df = df[[col for col in df if df[col].nunique() > 1]]# keep columns where there are more than 1 unique values\n",
    "\n",
    "corr = df.corr()\n",
    "\n",
    "plt.figure(figsize=(15,12))\n",
    "\n",
    "sns.heatmap(corr)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9938277978738366"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['num_root'].corr(df['num_compromised'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9983615072725952"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['srv_serror_rate'].corr(df['serror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9436670688882655"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['srv_count'].corr(df['count'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9947309539817937"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['srv_rerror_rate'].corr(df['rerror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9736854572953983"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_same_srv_rate'].corr(df['dst_host_srv_count'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9981559173373309"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_srv_serror_rate'].corr(df['dst_host_serror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9848038371110298"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_srv_rerror_rate'].corr(df['dst_host_rerror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9278080342691242"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_same_srv_rate'].corr(df['same_srv_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8989546630324209"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_srv_count'].corr(df['same_srv_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9449263676783333"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_same_src_port_rate'].corr(df['srv_count'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9986729680105015"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_serror_rate'].corr(df['serror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.997835300373975"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_serror_rate'].corr(df['srv_serror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9978492485680104"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_srv_serror_rate'].corr(df['serror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9993041091850098"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_srv_serror_rate'].corr(df['srv_serror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9869947924956001"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_rerror_rate'].corr(df['rerror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9821663427308375"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_rerror_rate'].corr(df['srv_rerror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9851995540751249"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_srv_rerror_rate'].corr(df['rerror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9865705438845669"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dst_host_srv_rerror_rate'].corr(df['srv_rerror_rate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "#This variable is highly correlated with num_compromised and should be ignored for analysis.\n",
    "#(Correlation = 0.9938277978738366)\n",
    "df.drop('num_root',axis = 1,inplace = True)\n",
    "\n",
    "#This variable is highly correlated with serror_rate and should be ignored for analysis.\n",
    "#(Correlation = 0.9983615072725952)\n",
    "df.drop('srv_serror_rate',axis = 1,inplace = True)\n",
    "\n",
    "#This variable is highly correlated with rerror_rate and should be ignored for analysis.\n",
    "#(Correlation = 0.9947309539817937)\n",
    "df.drop('srv_rerror_rate',axis = 1, inplace=True)\n",
    "\n",
    "#This variable is highly correlated with srv_serror_rate and should be ignored for analysis.\n",
    "#(Correlation = 0.9993041091850098)\n",
    "df.drop('dst_host_srv_serror_rate',axis = 1, inplace=True)\n",
    "\n",
    "#This variable is highly correlated with rerror_rate and should be ignored for analysis.\n",
    "#(Correlation = 0.9869947924956001)\n",
    "df.drop('dst_host_serror_rate',axis = 1, inplace=True)\n",
    "\n",
    "#This variable is highly correlated with srv_rerror_rate and should be ignored for analysis.\n",
    "#(Correlation = 0.9821663427308375)\n",
    "df.drop('dst_host_rerror_rate',axis = 1, inplace=True)\n",
    "\n",
    "#This variable is highly correlated with rerror_rate and should be ignored for analysis.\n",
    "#(Correlation = 0.9851995540751249)\n",
    "df.drop('dst_host_srv_rerror_rate',axis = 1, inplace=True)\n",
    "\n",
    "#This variable is highly correlated with dst_host_srv_count and should be ignored for analysis.\n",
    "#(Correlation = 0.9865705438845669)\n",
    "df.drop('dst_host_same_srv_rate',axis = 1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>duration</th>\n",
       "      <th>protocol_type</th>\n",
       "      <th>service</th>\n",
       "      <th>flag</th>\n",
       "      <th>src_bytes</th>\n",
       "      <th>dst_bytes</th>\n",
       "      <th>land</th>\n",
       "      <th>wrong_fragment</th>\n",
       "      <th>urgent</th>\n",
       "      <th>hot</th>\n",
       "      <th>...</th>\n",
       "      <th>same_srv_rate</th>\n",
       "      <th>diff_srv_rate</th>\n",
       "      <th>srv_diff_host_rate</th>\n",
       "      <th>dst_host_count</th>\n",
       "      <th>dst_host_srv_count</th>\n",
       "      <th>dst_host_diff_srv_rate</th>\n",
       "      <th>dst_host_same_src_port_rate</th>\n",
       "      <th>dst_host_srv_diff_host_rate</th>\n",
       "      <th>target</th>\n",
       "      <th>Attack Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>181</td>\n",
       "      <td>5450</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.11</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>239</td>\n",
       "      <td>486</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>19</td>\n",
       "      <td>19</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.05</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>235</td>\n",
       "      <td>1337</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>29</td>\n",
       "      <td>29</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>219</td>\n",
       "      <td>1337</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>39</td>\n",
       "      <td>39</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>tcp</td>\n",
       "      <td>http</td>\n",
       "      <td>SF</td>\n",
       "      <td>217</td>\n",
       "      <td>2032</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>49</td>\n",
       "      <td>49</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.02</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 33 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   duration protocol_type service flag  src_bytes  dst_bytes  land  \\\n",
       "0         0           tcp    http   SF        181       5450     0   \n",
       "1         0           tcp    http   SF        239        486     0   \n",
       "2         0           tcp    http   SF        235       1337     0   \n",
       "3         0           tcp    http   SF        219       1337     0   \n",
       "4         0           tcp    http   SF        217       2032     0   \n",
       "\n",
       "   wrong_fragment  urgent  hot  ...  same_srv_rate  diff_srv_rate  \\\n",
       "0               0       0    0  ...            1.0            0.0   \n",
       "1               0       0    0  ...            1.0            0.0   \n",
       "2               0       0    0  ...            1.0            0.0   \n",
       "3               0       0    0  ...            1.0            0.0   \n",
       "4               0       0    0  ...            1.0            0.0   \n",
       "\n",
       "   srv_diff_host_rate  dst_host_count  dst_host_srv_count  \\\n",
       "0                 0.0               9                   9   \n",
       "1                 0.0              19                  19   \n",
       "2                 0.0              29                  29   \n",
       "3                 0.0              39                  39   \n",
       "4                 0.0              49                  49   \n",
       "\n",
       "   dst_host_diff_srv_rate  dst_host_same_src_port_rate  \\\n",
       "0                     0.0                         0.11   \n",
       "1                     0.0                         0.05   \n",
       "2                     0.0                         0.03   \n",
       "3                     0.0                         0.03   \n",
       "4                     0.0                         0.02   \n",
       "\n",
       "   dst_host_srv_diff_host_rate   target  Attack Type  \n",
       "0                          0.0  normal.       normal  \n",
       "1                          0.0  normal.       normal  \n",
       "2                          0.0  normal.       normal  \n",
       "3                          0.0  normal.       normal  \n",
       "4                          0.0  normal.       normal  \n",
       "\n",
       "[5 rows x 33 columns]"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(494021, 33)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['duration', 'protocol_type', 'service', 'flag', 'src_bytes',\n",
       "       'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',\n",
       "       'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',\n",
       "       'su_attempted', 'num_file_creations', 'num_shells', 'num_access_files',\n",
       "       'is_guest_login', 'count', 'srv_count', 'serror_rate', 'rerror_rate',\n",
       "       'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',\n",
       "       'dst_host_count', 'dst_host_srv_count', 'dst_host_diff_srv_rate',\n",
       "       'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'target',\n",
       "       'Attack Type'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "urgent                              0.005510\n",
       "land                                0.006673\n",
       "su_attempted                        0.007793\n",
       "root_shell                          0.010551\n",
       "num_shells                          0.011020\n",
       "num_failed_logins                   0.015520\n",
       "num_access_files                    0.036482\n",
       "is_guest_login                      0.037211\n",
       "dst_host_srv_diff_host_rate         0.042133\n",
       "diff_srv_rate                       0.082205\n",
       "num_file_creations                  0.096416\n",
       "dst_host_diff_srv_rate              0.109259\n",
       "wrong_fragment                      0.134805\n",
       "srv_diff_host_rate                  0.142397\n",
       "rerror_rate                         0.231623\n",
       "logged_in                           0.355345\n",
       "serror_rate                         0.380717\n",
       "same_srv_rate                       0.388189\n",
       "dst_host_same_src_port_rate         0.481309\n",
       "hot                                 0.782103\n",
       "num_compromised                     1.798326\n",
       "dst_host_count                     64.745380\n",
       "dst_host_srv_count                106.040437\n",
       "count                             213.147412\n",
       "srv_count                         246.322817\n",
       "duration                          707.746472\n",
       "dst_bytes                       33040.001252\n",
       "src_bytes                      988218.101050\n",
       "dtype: float64"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_std = df.std()\n",
    "df_std = df_std.sort_values(ascending = True)\n",
    "df_std"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "FEATURE MAPPING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "icmp    283602\n",
       "tcp     190065\n",
       "udp      20354\n",
       "Name: protocol_type, dtype: int64"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['protocol_type'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "#protocol_type feature mapping\n",
    "pmap = {'icmp':0,'tcp':1,'udp':2}\n",
    "df['protocol_type'] = df['protocol_type'].map(pmap)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SF        378440\n",
       "S0         87007\n",
       "REJ        26875\n",
       "RSTR         903\n",
       "RSTO         579\n",
       "SH           107\n",
       "S1            57\n",
       "S2            24\n",
       "RSTOS0        11\n",
       "S3            10\n",
       "OTH            8\n",
       "Name: flag, dtype: int64"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['flag'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "#flag feature mapping\n",
    "fmap = {'SF':0,'S0':1,'REJ':2,'RSTR':3,'RSTO':4,'SH':5 ,'S1':6 ,'S2':7,'RSTOS0':8,'S3':9 ,'OTH':10}\n",
    "df['flag'] = df['flag'].map(fmap)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>duration</th>\n",
       "      <th>protocol_type</th>\n",
       "      <th>service</th>\n",
       "      <th>flag</th>\n",
       "      <th>src_bytes</th>\n",
       "      <th>dst_bytes</th>\n",
       "      <th>land</th>\n",
       "      <th>wrong_fragment</th>\n",
       "      <th>urgent</th>\n",
       "      <th>hot</th>\n",
       "      <th>...</th>\n",
       "      <th>same_srv_rate</th>\n",
       "      <th>diff_srv_rate</th>\n",
       "      <th>srv_diff_host_rate</th>\n",
       "      <th>dst_host_count</th>\n",
       "      <th>dst_host_srv_count</th>\n",
       "      <th>dst_host_diff_srv_rate</th>\n",
       "      <th>dst_host_same_src_port_rate</th>\n",
       "      <th>dst_host_srv_diff_host_rate</th>\n",
       "      <th>target</th>\n",
       "      <th>Attack Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>http</td>\n",
       "      <td>0</td>\n",
       "      <td>181</td>\n",
       "      <td>5450</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.11</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>http</td>\n",
       "      <td>0</td>\n",
       "      <td>239</td>\n",
       "      <td>486</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>19</td>\n",
       "      <td>19</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.05</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>http</td>\n",
       "      <td>0</td>\n",
       "      <td>235</td>\n",
       "      <td>1337</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>29</td>\n",
       "      <td>29</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>http</td>\n",
       "      <td>0</td>\n",
       "      <td>219</td>\n",
       "      <td>1337</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>39</td>\n",
       "      <td>39</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>http</td>\n",
       "      <td>0</td>\n",
       "      <td>217</td>\n",
       "      <td>2032</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>49</td>\n",
       "      <td>49</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.02</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 33 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   duration  protocol_type service  flag  src_bytes  dst_bytes  land  \\\n",
       "0         0              1    http     0        181       5450     0   \n",
       "1         0              1    http     0        239        486     0   \n",
       "2         0              1    http     0        235       1337     0   \n",
       "3         0              1    http     0        219       1337     0   \n",
       "4         0              1    http     0        217       2032     0   \n",
       "\n",
       "   wrong_fragment  urgent  hot  ...  same_srv_rate  diff_srv_rate  \\\n",
       "0               0       0    0  ...            1.0            0.0   \n",
       "1               0       0    0  ...            1.0            0.0   \n",
       "2               0       0    0  ...            1.0            0.0   \n",
       "3               0       0    0  ...            1.0            0.0   \n",
       "4               0       0    0  ...            1.0            0.0   \n",
       "\n",
       "   srv_diff_host_rate  dst_host_count  dst_host_srv_count  \\\n",
       "0                 0.0               9                   9   \n",
       "1                 0.0              19                  19   \n",
       "2                 0.0              29                  29   \n",
       "3                 0.0              39                  39   \n",
       "4                 0.0              49                  49   \n",
       "\n",
       "   dst_host_diff_srv_rate  dst_host_same_src_port_rate  \\\n",
       "0                     0.0                         0.11   \n",
       "1                     0.0                         0.05   \n",
       "2                     0.0                         0.03   \n",
       "3                     0.0                         0.03   \n",
       "4                     0.0                         0.02   \n",
       "\n",
       "   dst_host_srv_diff_host_rate   target  Attack Type  \n",
       "0                          0.0  normal.       normal  \n",
       "1                          0.0  normal.       normal  \n",
       "2                          0.0  normal.       normal  \n",
       "3                          0.0  normal.       normal  \n",
       "4                          0.0  normal.       normal  \n",
       "\n",
       "[5 rows x 33 columns]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop('service',axis = 1,inplace= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(494021, 32)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>duration</th>\n",
       "      <th>protocol_type</th>\n",
       "      <th>flag</th>\n",
       "      <th>src_bytes</th>\n",
       "      <th>dst_bytes</th>\n",
       "      <th>land</th>\n",
       "      <th>wrong_fragment</th>\n",
       "      <th>urgent</th>\n",
       "      <th>hot</th>\n",
       "      <th>num_failed_logins</th>\n",
       "      <th>...</th>\n",
       "      <th>same_srv_rate</th>\n",
       "      <th>diff_srv_rate</th>\n",
       "      <th>srv_diff_host_rate</th>\n",
       "      <th>dst_host_count</th>\n",
       "      <th>dst_host_srv_count</th>\n",
       "      <th>dst_host_diff_srv_rate</th>\n",
       "      <th>dst_host_same_src_port_rate</th>\n",
       "      <th>dst_host_srv_diff_host_rate</th>\n",
       "      <th>target</th>\n",
       "      <th>Attack Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>181</td>\n",
       "      <td>5450</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.11</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>239</td>\n",
       "      <td>486</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>19</td>\n",
       "      <td>19</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.05</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>235</td>\n",
       "      <td>1337</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>29</td>\n",
       "      <td>29</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>219</td>\n",
       "      <td>1337</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>39</td>\n",
       "      <td>39</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>217</td>\n",
       "      <td>2032</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>49</td>\n",
       "      <td>49</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.02</td>\n",
       "      <td>0.0</td>\n",
       "      <td>normal.</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 32 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   duration  protocol_type  flag  src_bytes  dst_bytes  land  wrong_fragment  \\\n",
       "0         0              1     0        181       5450     0               0   \n",
       "1         0              1     0        239        486     0               0   \n",
       "2         0              1     0        235       1337     0               0   \n",
       "3         0              1     0        219       1337     0               0   \n",
       "4         0              1     0        217       2032     0               0   \n",
       "\n",
       "   urgent  hot  num_failed_logins  ...  same_srv_rate  diff_srv_rate  \\\n",
       "0       0    0                  0  ...            1.0            0.0   \n",
       "1       0    0                  0  ...            1.0            0.0   \n",
       "2       0    0                  0  ...            1.0            0.0   \n",
       "3       0    0                  0  ...            1.0            0.0   \n",
       "4       0    0                  0  ...            1.0            0.0   \n",
       "\n",
       "   srv_diff_host_rate  dst_host_count  dst_host_srv_count  \\\n",
       "0                 0.0               9                   9   \n",
       "1                 0.0              19                  19   \n",
       "2                 0.0              29                  29   \n",
       "3                 0.0              39                  39   \n",
       "4                 0.0              49                  49   \n",
       "\n",
       "   dst_host_diff_srv_rate  dst_host_same_src_port_rate  \\\n",
       "0                     0.0                         0.11   \n",
       "1                     0.0                         0.05   \n",
       "2                     0.0                         0.03   \n",
       "3                     0.0                         0.03   \n",
       "4                     0.0                         0.02   \n",
       "\n",
       "   dst_host_srv_diff_host_rate   target  Attack Type  \n",
       "0                          0.0  normal.       normal  \n",
       "1                          0.0  normal.       normal  \n",
       "2                          0.0  normal.       normal  \n",
       "3                          0.0  normal.       normal  \n",
       "4                          0.0  normal.       normal  \n",
       "\n",
       "[5 rows x 32 columns]"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "duration                         int64\n",
       "protocol_type                    int64\n",
       "flag                             int64\n",
       "src_bytes                        int64\n",
       "dst_bytes                        int64\n",
       "land                             int64\n",
       "wrong_fragment                   int64\n",
       "urgent                           int64\n",
       "hot                              int64\n",
       "num_failed_logins                int64\n",
       "logged_in                        int64\n",
       "num_compromised                  int64\n",
       "root_shell                       int64\n",
       "su_attempted                     int64\n",
       "num_file_creations               int64\n",
       "num_shells                       int64\n",
       "num_access_files                 int64\n",
       "is_guest_login                   int64\n",
       "count                            int64\n",
       "srv_count                        int64\n",
       "serror_rate                    float64\n",
       "rerror_rate                    float64\n",
       "same_srv_rate                  float64\n",
       "diff_srv_rate                  float64\n",
       "srv_diff_host_rate             float64\n",
       "dst_host_count                   int64\n",
       "dst_host_srv_count               int64\n",
       "dst_host_diff_srv_rate         float64\n",
       "dst_host_same_src_port_rate    float64\n",
       "dst_host_srv_diff_host_rate    float64\n",
       "target                          object\n",
       "Attack Type                     object\n",
       "dtype: object"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "MODELLING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(494021, 31)\n",
      "(330994, 30) (163027, 30)\n",
      "(330994, 1) (163027, 1)\n"
     ]
    }
   ],
   "source": [
    "df = df.drop(['target',], axis=1)\n",
    "print(df.shape)\n",
    "\n",
    "# Target variable and train set\n",
    "Y = df[['Attack Type']]\n",
    "X = df.drop(['Attack Type',], axis=1)\n",
    "\n",
    "sc = MinMaxScaler()\n",
    "X = sc.fit_transform(X)\n",
    "\n",
    "# Split test and train data \n",
    "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)\n",
    "print(X_train.shape, X_test.shape)\n",
    "print(Y_train.shape, Y_test.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "GAUSSIAN NAIVE BAYES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Gaussian Naive Bayes\n",
    "from sklearn.naive_bayes import GaussianNB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "model1 = GaussianNB()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "model1.fit(X_train, Y_train.values.ravel())\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training time:  1.0472145080566406\n"
     ]
    }
   ],
   "source": [
    "print(\"Training time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "Y_test_pred1 = model1.predict(X_test)\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Testing time:  0.7908921241760254\n"
     ]
    }
   ],
   "source": [
    "print(\"Testing time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train score is: 0.8795114110829804\n",
      "Test score is: 0.8790384414851528\n"
     ]
    }
   ],
   "source": [
    "print(\"Train score is:\", model1.score(X_train, Y_train))\n",
    "print(\"Test score is:\",model1.score(X_test,Y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "DECISION TREE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Decision Tree \n",
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "model2 = DecisionTreeClassifier(criterion=\"entropy\", max_depth = 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "model2.fit(X_train, Y_train.values.ravel())\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training time:  1.504838466644287\n"
     ]
    }
   ],
   "source": [
    "print(\"Training time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "Y_test_pred2 = model2.predict(X_test)\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Testing time:  0.10471415519714355\n"
     ]
    }
   ],
   "source": [
    "print(\"Testing time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train score is: 0.9905829108684749\n",
      "Test score is: 0.9905230421954646\n"
     ]
    }
   ],
   "source": [
    "print(\"Train score is:\", model2.score(X_train, Y_train))\n",
    "print(\"Test score is:\",model2.score(X_test,Y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "RANDOM FOREST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "model3 = RandomForestClassifier(n_estimators=30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "model3.fit(X_train, Y_train.values.ravel())\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training time:  11.453320026397705\n"
     ]
    }
   ],
   "source": [
    "print(\"Training time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "Y_test_pred3 = model3.predict(X_test)\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Testing time:  0.6096138954162598\n"
     ]
    }
   ],
   "source": [
    "print(\"Testing time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train score is: 0.99997583037759\n",
      "Test score is: 0.9996994362896944\n"
     ]
    }
   ],
   "source": [
    "print(\"Train score is:\", model3.score(X_train, Y_train))\n",
    "print(\"Test score is:\",model3.score(X_test,Y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "SUPPORT VECTOR MACHINE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.svm import SVC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "model4 = SVC(gamma = 'scale')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "model4.fit(X_train, Y_train.values.ravel())\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training time:  126.96016049385071\n"
     ]
    }
   ],
   "source": [
    "print(\"Training time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "Y_test_pred4 = model4.predict(X_test)\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Testing time:  32.726547718048096\n"
     ]
    }
   ],
   "source": [
    "print(\"Testing time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train score is: 0.9987552644458811\n",
      "Test score is: 0.9987916112055059\n"
     ]
    }
   ],
   "source": [
    "print(\"Train score is:\", model4.score(X_train, Y_train))\n",
    "print(\"Test score is:\", model4.score(X_test,Y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "LOGISTIC REGRESSION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "model5 = LogisticRegression(max_iter=1200000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "model5.fit(X_train, Y_train.values.ravel())\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training time:  56.67286133766174\n"
     ]
    }
   ],
   "source": [
    "print(\"Training time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "Y_test_pred5 = model5.predict(X_test)\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Testing time:  0.02198958396911621\n"
     ]
    }
   ],
   "source": [
    "print(\"Testing time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train score is: 0.9935285835997028\n",
      "Test score is: 0.9935286792985211\n"
     ]
    }
   ],
   "source": [
    "print(\"Train score is:\", model5.score(X_train, Y_train))\n",
    "print(\"Test score is:\",model5.score(X_test,Y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "GRADIENT BOOSTING CLASSIFIER"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import GradientBoostingClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "model6 = GradientBoostingClassifier(random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "model6.fit(X_train, Y_train.values.ravel())\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training time:  446.690997838974\n"
     ]
    }
   ],
   "source": [
    "print(\"Training time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "Y_test_pred6 = model6.predict(X_test)\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Testing time:  1.4141650199890137\n"
     ]
    }
   ],
   "source": [
    "print(\"Testing time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train score is: 0.9979304760811374\n",
      "Test score is: 0.9977181693829856\n"
     ]
    }
   ],
   "source": [
    "print(\"Train score is:\", model6.score(X_train, Y_train))\n",
    "print(\"Test score is:\", model6.score(X_test,Y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Artificial Neural Network"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Using TensorFlow backend.\n"
     ]
    }
   ],
   "source": [
    "from keras.models import Sequential\n",
    "from keras.layers import Dense\n",
    "from keras.wrappers.scikit_learn import KerasClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun():\n",
    "    model = Sequential()\n",
    "    \n",
    "    #here 30 is output dimension\n",
    "    model.add(Dense(30,input_dim =30,activation = 'relu',kernel_initializer='random_uniform'))\n",
    "    \n",
    "    #in next layer we do not specify the input_dim as the model is sequential so output of previous layer is input to next layer\n",
    "    model.add(Dense(1,activation='sigmoid',kernel_initializer='random_uniform'))\n",
    "    \n",
    "    #5 classes-normal,dos,probe,r2l,u2r\n",
    "    model.add(Dense(5,activation='softmax'))\n",
    "    \n",
    "    #loss is categorical_crossentropy which specifies that we have multiple classes\n",
    "    \n",
    "    model.compile(loss ='categorical_crossentropy',optimizer = 'adam',metrics = ['accuracy'])\n",
    "    \n",
    "    return model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Since,the dataset is very big and we cannot fit complete data at once so we use batch size.\n",
    "#This divides our data into batches each of size equal to batch_size.\n",
    "#Now only this number of samples will be loaded into memory and processed. \n",
    "#Once we are done with one batch it is flushed from memory and the next batch will be processed.\n",
    "model7 = KerasClassifier(build_fn=fun,epochs=100,batch_size=64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/100\n",
      "330994/330994 [==============================] - 8s 24us/step - loss: 0.5521 - accuracy: 0.9682\n",
      "Epoch 2/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.1555 - accuracy: 0.9845\n",
      "Epoch 3/100\n",
      "330994/330994 [==============================] - 6s 17us/step - loss: 0.0974 - accuracy: 0.9845\n",
      "Epoch 4/100\n",
      "330994/330994 [==============================] - 6s 17us/step - loss: 0.0849 - accuracy: 0.9846\n",
      "Epoch 5/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0804 - accuracy: 0.9846\n",
      "Epoch 6/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0730 - accuracy: 0.9845\n",
      "Epoch 7/100\n",
      "330994/330994 [==============================] - 6s 20us/step - loss: 0.0698 - accuracy: 0.9846\n",
      "Epoch 8/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0683 - accuracy: 0.9846\n",
      "Epoch 9/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0672 - accuracy: 0.9846\n",
      "Epoch 10/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0664 - accuracy: 0.9846\n",
      "Epoch 11/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0658 - accuracy: 0.9846\n",
      "Epoch 12/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0653 - accuracy: 0.9847\n",
      "Epoch 13/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0649 - accuracy: 0.9847\n",
      "Epoch 14/100\n",
      "330994/330994 [==============================] - 8s 24us/step - loss: 0.0646 - accuracy: 0.9847\n",
      "Epoch 15/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0643 - accuracy: 0.9847\n",
      "Epoch 16/100\n",
      "330994/330994 [==============================] - 6s 17us/step - loss: 0.0640 - accuracy: 0.9847\n",
      "Epoch 17/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0637 - accuracy: 0.9847\n",
      "Epoch 18/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0634 - accuracy: 0.9847\n",
      "Epoch 19/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0632 - accuracy: 0.9847\n",
      "Epoch 20/100\n",
      "330994/330994 [==============================] - 8s 24us/step - loss: 0.0629 - accuracy: 0.9847\n",
      "Epoch 21/100\n",
      "330994/330994 [==============================] - 8s 24us/step - loss: 0.0627 - accuracy: 0.9847\n",
      "Epoch 22/100\n",
      "330994/330994 [==============================] - 8s 25us/step - loss: 0.0625 - accuracy: 0.9847\n",
      "Epoch 23/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0623 - accuracy: 0.9847\n",
      "Epoch 24/100\n",
      "330994/330994 [==============================] - 8s 24us/step - loss: 0.0621 - accuracy: 0.9847\n",
      "Epoch 25/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0619 - accuracy: 0.9847\n",
      "Epoch 26/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0618 - accuracy: 0.9847\n",
      "Epoch 27/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0616 - accuracy: 0.9847\n",
      "Epoch 28/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0614 - accuracy: 0.9847\n",
      "Epoch 29/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0613 - accuracy: 0.9847\n",
      "Epoch 30/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0611 - accuracy: 0.9847\n",
      "Epoch 31/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0610 - accuracy: 0.9847\n",
      "Epoch 32/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0609 - accuracy: 0.9847\n",
      "Epoch 33/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0607 - accuracy: 0.9847\n",
      "Epoch 34/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0606 - accuracy: 0.9847\n",
      "Epoch 35/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0605 - accuracy: 0.9847\n",
      "Epoch 36/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0604 - accuracy: 0.9847\n",
      "Epoch 37/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0603 - accuracy: 0.9847\n",
      "Epoch 38/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0601 - accuracy: 0.9847\n",
      "Epoch 39/100\n",
      "330994/330994 [==============================] - 8s 23us/step - loss: 0.0600 - accuracy: 0.9847\n",
      "Epoch 40/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0599 - accuracy: 0.9847\n",
      "Epoch 41/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0598 - accuracy: 0.9847\n",
      "Epoch 42/100\n",
      "330994/330994 [==============================] - 7s 23us/step - loss: 0.0597 - accuracy: 0.9847\n",
      "Epoch 43/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0596 - accuracy: 0.9847\n",
      "Epoch 44/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0595 - accuracy: 0.9847\n",
      "Epoch 45/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0594 - accuracy: 0.9847\n",
      "Epoch 46/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0593 - accuracy: 0.9847\n",
      "Epoch 47/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0592 - accuracy: 0.9847\n",
      "Epoch 48/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0591 - accuracy: 0.9847\n",
      "Epoch 49/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0590 - accuracy: 0.9847\n",
      "Epoch 50/100\n",
      "330994/330994 [==============================] - 6s 18us/step - loss: 0.0590 - accuracy: 0.9847\n",
      "Epoch 51/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0589 - accuracy: 0.9847\n",
      "Epoch 52/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0588 - accuracy: 0.9847\n",
      "Epoch 53/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0587 - accuracy: 0.9847\n",
      "Epoch 54/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0586 - accuracy: 0.9847\n",
      "Epoch 55/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0585 - accuracy: 0.9848\n",
      "Epoch 56/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0584 - accuracy: 0.9847\n",
      "Epoch 57/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0584 - accuracy: 0.9847\n",
      "Epoch 58/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0583 - accuracy: 0.9848\n",
      "Epoch 59/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0582 - accuracy: 0.9847\n",
      "Epoch 60/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0581 - accuracy: 0.9848\n",
      "Epoch 61/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0581 - accuracy: 0.9848\n",
      "Epoch 62/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0580 - accuracy: 0.9848\n",
      "Epoch 63/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0579 - accuracy: 0.9847\n",
      "Epoch 64/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0578 - accuracy: 0.9847\n",
      "Epoch 65/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0578 - accuracy: 0.9848\n",
      "Epoch 66/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0577 - accuracy: 0.9848\n",
      "Epoch 67/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0576 - accuracy: 0.9848\n",
      "Epoch 68/100\n",
      "330994/330994 [==============================] - 6s 20us/step - loss: 0.0576 - accuracy: 0.9848\n",
      "Epoch 69/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0575 - accuracy: 0.9848\n",
      "Epoch 70/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0574 - accuracy: 0.9848\n",
      "Epoch 71/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0574 - accuracy: 0.9848\n",
      "Epoch 72/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0573 - accuracy: 0.9848\n",
      "Epoch 73/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0573 - accuracy: 0.9848\n",
      "Epoch 74/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0572 - accuracy: 0.9848\n",
      "Epoch 75/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0571 - accuracy: 0.9848\n",
      "Epoch 76/100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0571 - accuracy: 0.9848\n",
      "Epoch 77/100\n",
      "330994/330994 [==============================] - 6s 20us/step - loss: 0.0570 - accuracy: 0.9848\n",
      "Epoch 78/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0570 - accuracy: 0.9848\n",
      "Epoch 79/100\n",
      "330994/330994 [==============================] - 7s 22us/step - loss: 0.0569 - accuracy: 0.9848\n",
      "Epoch 80/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0568 - accuracy: 0.9848\n",
      "Epoch 81/100\n",
      "330994/330994 [==============================] - 8s 24us/step - loss: 0.0568 - accuracy: 0.9848\n",
      "Epoch 82/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0567 - accuracy: 0.9848\n",
      "Epoch 83/100\n",
      "330994/330994 [==============================] - 8s 23us/step - loss: 0.0567 - accuracy: 0.9848\n",
      "Epoch 84/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0566 - accuracy: 0.9848\n",
      "Epoch 85/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0566 - accuracy: 0.9848\n",
      "Epoch 86/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0565 - accuracy: 0.9848\n",
      "Epoch 87/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0565 - accuracy: 0.9848\n",
      "Epoch 88/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0564 - accuracy: 0.9848\n",
      "Epoch 89/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0564 - accuracy: 0.9848\n",
      "Epoch 90/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0563 - accuracy: 0.9848\n",
      "Epoch 91/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0563 - accuracy: 0.9848\n",
      "Epoch 92/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0562 - accuracy: 0.9848\n",
      "Epoch 93/100\n",
      "330994/330994 [==============================] - 6s 19us/step - loss: 0.0562 - accuracy: 0.9848\n",
      "Epoch 94/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0561 - accuracy: 0.9848\n",
      "Epoch 95/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0560 - accuracy: 0.9848\n",
      "Epoch 96/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0559 - accuracy: 0.9848\n",
      "Epoch 97/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0555 - accuracy: 0.9848\n",
      "Epoch 98/100\n",
      "330994/330994 [==============================] - 7s 20us/step - loss: 0.0546 - accuracy: 0.9848\n",
      "Epoch 99/100\n",
      "330994/330994 [==============================] - 6s 20us/step - loss: 0.0533 - accuracy: 0.9847\n",
      "Epoch 100/100\n",
      "330994/330994 [==============================] - 7s 21us/step - loss: 0.0497 - accuracy: 0.9848\n"
     ]
    }
   ],
   "source": [
    "start = time.time()\n",
    "model7.fit(X_train, Y_train.values.ravel())\n",
    "end = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training time\n",
      "674.1276211738586\n"
     ]
    }
   ],
   "source": [
    "print('Training time')\n",
    "print((end-start))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "Y_test_pred7 = model7.predict(X_test)\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Testing time:  0.9642157554626465\n"
     ]
    }
   ],
   "source": [
    "print(\"Testing time: \",end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "Y_train_pred7 = model7.predict(X_train)\n",
    "end_time = time.time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9848547103572874"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(Y_train,Y_train_pred7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9847203224005839"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(Y_test,Y_test_pred7)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "TRAINING ACCURACY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 7 artists>"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "names = ['NB','DT','RF','SVM','LR','GB','ANN']\n",
    "values = [87.951,99.058,99.997,99.875,99.352,99.793,98.485]\n",
    "f = plt.figure(figsize=(15,3),num=10)\n",
    "plt.subplot(131)\n",
    "plt.ylim(80,102)\n",
    "plt.bar(names,values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "f.savefig('training_accuracy_figure.png',bbox_inches='tight')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "TESTING ACCURACY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 7 artists>"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "names = ['NB','DT','RF','SVM','LR','GB','ANN']\n",
    "values = [87.903,99.052,99.969,99.879,99.352,99.771,98.472]\n",
    "f = plt.figure(figsize=(15,3),num=10)\n",
    "plt.subplot(131)\n",
    "plt.ylim(80,102)\n",
    "plt.bar(names,values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "f.savefig('test_accuracy_figure.png',bbox_inches='tight')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "TRAINING TIME"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 7 artists>"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "names = ['NB','DT','RF','SVM','LR','GB','ANN']\n",
    "values = [1.04721,1.50483,11.45332,126.96016,56.67286,446.69099,674.12762]\n",
    "f = plt.figure(figsize=(15,3),num=10)\n",
    "plt.subplot(131)\n",
    "plt.bar(names,values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "f.savefig('train_time_figure.png',bbox_inches='tight')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "TESTING TIME"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 7 artists>"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "names = ['NB','DT','RF','SVM','LR','GB','ANN']\n",
    "values = [0.79089,0.10471,0.60961,32.72654,0.02198,1.41416,0.96421]\n",
    "f = plt.figure(figsize=(15,3),num=10)\n",
    "plt.subplot(131)\n",
    "plt.bar(names,values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [],
   "source": [
    "f.savefig('test_time_figure.png',bbox_inches='tight')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": nullcontext,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "gputest",
   "language": "python",
   "name": "gputest"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
