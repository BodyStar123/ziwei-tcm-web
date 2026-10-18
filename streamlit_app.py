{\rtf1\ansi\ansicpg950\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red252\green99\blue95;\red12\green14\blue18;\red224\green232\blue240;
\red253\green149\blue70;\red198\green146\blue255;\red150\green204\blue255;\red120\green129\blue140;\red104\green177\blue255;
}
{\*\expandedcolortbl;;\cssrgb\c100000\c48235\c44706;\cssrgb\c5098\c6667\c9020;\cssrgb\c90196\c92941\c95294;
\cssrgb\c100000\c65098\c34118;\cssrgb\c82353\c65882\c100000;\cssrgb\c64706\c83922\c100000;\cssrgb\c54510\c58039\c61961;\cssrgb\c47451\c75294\c100000;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 streamlit\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 st\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  \cf5 \strokec5 lunar_python\cf4 \strokec4  \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 Solar\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  \cf5 \strokec5 google\cf4 \strokec4  \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 genai\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 st\cf4 \strokec4 .\cf6 \strokec6 set_page_config\cf4 \strokec4 (\cf5 \strokec5 page_title\cf2 \strokec2 =\cf7 \strokec7 "\uc0\u32043 \u24494 \u26007 \u25976  \'d7 \u20013 \u37291 \u32147 \u32097 \u26234 \u24935 \u25490 \u30436 \u31995 \u32113 "\cf4 \strokec4 , \cf5 \strokec5 layout\cf2 \strokec2 =\cf7 \strokec7 "centered"\cf4 \strokec4 )\cb1 \
\
\cf5 \cb3 \strokec5 st\cf4 \strokec4 .title(\cf7 \strokec7 "\uc0\u55356 \u57119  \u32043 \u24494 \u26007 \u25976  \'d7 \u20013 \u37291 \u32147 \u32097 \u26234 \u24935 \u25490 \u30436 \u31995 \u32113 "\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 st\cf4 \strokec4 .markdown(\cf7 \strokec7 "\uc0\u36664 \u20837 \u20320 \u30340 \u20986 \u29983 \u22283 \u26310 \u26178 \u38291 \u65292 \u21363 \u26178 \u35299 \u26512 \u32147 \u32097 \u27683 \u27231 \u12289 \u23470 \u20301 \u33287 \u30149 \u29702 \u21629 \u30436 \u65292 \u20006 \u36879 \u36942  AI \u36914 \u34892 \u25972 \u39636 \u33256 \u24202 \u21512 \u21443 \u65281 "\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 # \uc0\u36664 \u20837 \u20171 \u38754 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 col1, col2, col3 \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .columns(\cf9 \strokec9 3\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf4 \strokec4  col1:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     year \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .number_input(\cf7 \strokec7 "\uc0\u20986 \u29983 \u24180 \u20221  (\u35199 \u20803 )"\cf4 \strokec4 , \cf5 \strokec5 value\cf2 \strokec2 =\cf9 \strokec9 2000\cf4 \strokec4 , \cf5 \strokec5 step\cf2 \strokec2 =\cf9 \strokec9 1\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf4 \strokec4  col2:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     month \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .number_input(\cf7 \strokec7 "\uc0\u20986 \u29983 \u26376 \u20221 "\cf4 \strokec4 , \cf5 \strokec5 value\cf2 \strokec2 =\cf9 \strokec9 1\cf4 \strokec4 , \cf5 \strokec5 min_value\cf2 \strokec2 =\cf9 \strokec9 1\cf4 \strokec4 , \cf5 \strokec5 max_value\cf2 \strokec2 =\cf9 \strokec9 12\cf4 \strokec4 , \cf5 \strokec5 step\cf2 \strokec2 =\cf9 \strokec9 1\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf4 \strokec4  col3:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     day \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .number_input(\cf7 \strokec7 "\uc0\u20986 \u29983 \u26085 \u26399 "\cf4 \strokec4 , \cf5 \strokec5 value\cf2 \strokec2 =\cf9 \strokec9 1\cf4 \strokec4 , \cf5 \strokec5 min_value\cf2 \strokec2 =\cf9 \strokec9 1\cf4 \strokec4 , \cf5 \strokec5 max_value\cf2 \strokec2 =\cf9 \strokec9 31\cf4 \strokec4 , \cf5 \strokec5 step\cf2 \strokec2 =\cf9 \strokec9 1\cf4 \strokec4 )\cb1 \
\
\cb3 col4, col5 \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .columns(\cf9 \strokec9 2\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf4 \strokec4  col4:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     hour \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .number_input(\cf7 \strokec7 "\uc0\u20986 \u29983 \u23567 \u26178  (24\u23567 \u26178 \u21046 )"\cf4 \strokec4 , \cf5 \strokec5 value\cf2 \strokec2 =\cf9 \strokec9 6\cf4 \strokec4 , \cf5 \strokec5 min_value\cf2 \strokec2 =\cf9 \strokec9 0\cf4 \strokec4 , \cf5 \strokec5 max_value\cf2 \strokec2 =\cf9 \strokec9 23\cf4 \strokec4 , \cf5 \strokec5 step\cf2 \strokec2 =\cf9 \strokec9 1\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf4 \strokec4  col5:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     minute \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .number_input(\cf7 \strokec7 "\uc0\u20986 \u29983 \u20998 \u37912 "\cf4 \strokec4 , \cf5 \strokec5 value\cf2 \strokec2 =\cf9 \strokec9 0\cf4 \strokec4 , \cf5 \strokec5 min_value\cf2 \strokec2 =\cf9 \strokec9 0\cf4 \strokec4 , \cf5 \strokec5 max_value\cf2 \strokec2 =\cf9 \strokec9 59\cf4 \strokec4 , \cf5 \strokec5 step\cf2 \strokec2 =\cf9 \strokec9 1\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .button(\cf7 \strokec7 "\uc0\u10024  \u38283 \u22987 \u25490 \u30436 \u33287 \u35299 \u26512 "\cf4 \strokec4 , \cf5 \strokec5 type\cf2 \strokec2 =\cf7 \strokec7 "primary"\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 try\cf4 \strokec4 :\cb1 \
\cb3         solar \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 Solar\cf4 \strokec4 .\cf6 \strokec6 fromYmdHms\cf4 \strokec4 (\cf5 \strokec5 int\cf4 \strokec4 (year), \cf5 \strokec5 int\cf4 \strokec4 (month), \cf5 \strokec5 int\cf4 \strokec4 (day), \cf5 \strokec5 int\cf4 \strokec4 (hour), \cf5 \strokec5 int\cf4 \strokec4 (minute), \cf9 \strokec9 0\cf4 \strokec4 )\cb1 \
\cb3         lunar \cf2 \strokec2 =\cf4 \strokec4  solar.\cf6 \strokec6 getLunar\cf4 \strokec4 ()\cb1 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .success(\cf7 \strokec7 "\uc0\u25490 \u30436 \u35336 \u31639 \u25104 \u21151 \u65281 "\cf4 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3         \cf8 \strokec8 # 1. \uc0\u22522 \u30990 \u38499 \u21015 \u33287 \u35722 \u25976 \u23450 \u32681 \cf4 \cb1 \strokec4 \
\cb3         branches \cf2 \strokec2 =\cf4 \strokec4  [\cf7 \strokec7 '\uc0\u23376 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19985 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u23493 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u21359 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36784 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24051 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u21320 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u26410 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30003 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u37193 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25100 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20133 '\cf4 \strokec4 ]\cb1 \
\cb3         lunar_month \cf2 \strokec2 =\cf4 \strokec4  \cf6 \strokec6 abs\cf4 \strokec4 (lunar.\cf6 \strokec6 getMonth\cf4 \strokec4 ())  \cb1 \
\cb3         time_zhi \cf2 \strokec2 =\cf4 \strokec4  lunar.\cf6 \strokec6 getTimeZhi\cf4 \strokec4 ()       \cb1 \
\cb3         birth_time_index \cf2 \strokec2 =\cf4 \strokec4  branches.\cf6 \strokec6 index\cf4 \strokec4 (time_zhi) \cf2 \strokec2 +\cf4 \strokec4  \cf9 \strokec9 1\cf4 \cb1 \strokec4 \
\
\cb3         \cf8 \strokec8 # 2. \uc0\u32321 \u39636 \u20013 \u25991 \u39023 \u31034 \u22522 \u26412 \u36039 \u35338 \cf4 \cb1 \strokec4 \
\cb3         lunar_year_cn \cf2 \strokec2 =\cf4 \strokec4  lunar.\cf6 \strokec6 getYearInChinese\cf4 \strokec4 ()\cb1 \
\cb3         lunar_month_cn \cf2 \strokec2 =\cf4 \strokec4  lunar.\cf6 \strokec6 getMonthInChinese\cf4 \strokec4 ()\cb1 \
\cb3         lunar_day_cn \cf2 \strokec2 =\cf4 \strokec4  lunar.\cf6 \strokec6 getDayInChinese\cf4 \strokec4 ()\cb1 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .subheader(\cf7 \strokec7 "\uc0\u12304 \u22522 \u26412 \u26310 \u27861 \u33287 \u24178 \u25903 \u36039 \u35338 \u12305 "\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .write(\cf2 \strokec2 f\cf7 \strokec7 "**\uc0\u22283 \u26310 \u26178 \u38291 **\u65306 \cf2 \strokec2 \{\cf4 \strokec4 year\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u24180 \cf2 \strokec2 \{\cf4 \strokec4 month\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u26376 \cf2 \strokec2 \{\cf4 \strokec4 day\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u26085  \cf2 \strokec2 \{\cf4 \strokec4 hour\cf2 \strokec2 :02d\}\cf7 \strokec7 :\cf2 \strokec2 \{\cf4 \strokec4 minute\cf2 \strokec2 :02d\}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .write(\cf2 \strokec2 f\cf7 \strokec7 "**\uc0\u36786 \u26310 \u26085 \u26399 **\u65306 \cf2 \strokec2 \{\cf4 \strokec4 lunar_year_cn\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u24180 \cf2 \strokec2 \{\cf4 \strokec4 lunar_month_cn\cf2 \strokec2 \}\{\cf4 \strokec4 lunar_day_cn\cf2 \strokec2 \}\cf7 \strokec7  \cf2 \strokec2 \{\cf4 \strokec4 time_zhi\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u26178 "\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .write(\cf2 \strokec2 f\cf7 \strokec7 "**\uc0\u22235 \u26609 \u24178 \u25903 **\u65306 \cf2 \strokec2 \{\cf4 \strokec4 lunar.\cf6 \strokec6 getYearInGanZhi\cf4 \strokec4 ()\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u24180  | \cf2 \strokec2 \{\cf4 \strokec4 lunar.\cf6 \strokec6 getMonthInGanZhi\cf4 \strokec4 ()\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u26376  | \cf2 \strokec2 \{\cf4 \strokec4 lunar.\cf6 \strokec6 getDayInGanZhi\cf4 \strokec4 ()\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u26085  | \cf2 \strokec2 \{\cf4 \strokec4 lunar.\cf6 \strokec6 getTimeInGanZhi\cf4 \strokec4 ()\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u26178 "\cf4 \strokec4 )\cb1 \
\
\cb3         \cf8 \strokec8 # 3. \uc0\u23383 \u20856 \u36039 \u26009 \u24235 \cf4 \cb1 \strokec4 \
\cb3         branch_to_organ \cf2 \strokec2 =\cf4 \strokec4  \{\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u23376 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u23376 \u23470  (\u36275 \u23569 \u38525 \u33213 \u32147 )'\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19985 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u19985 \u23470  (\u36275 \u21413 \u38512 \u32925 \u32147 )'\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u23493 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u23493 \u23470  (\u25163 \u22826 \u38512 \u32954 \u32147 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u21359 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u21359 \u23470  (\u25163 \u38525 \u26126 \u22823 \u33144 \u32147 )'\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36784 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u36784 \u23470  (\u36275 \u38525 \u26126 \u32963 \u32147 )'\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24051 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u24051 \u23470  (\u36275 \u22826 \u38512 \u33086 \u32147 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u21320 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u21320 \u23470  (\u25163 \u23569 \u38512 \u24515 \u32147 )'\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u26410 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u26410 \u23470  (\u25163 \u22826 \u38525 \u23567 \u33144 \u32147 )'\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30003 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u30003 \u23470  (\u36275 \u22826 \u38525 \u33152 \u33009 \u32147 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u37193 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u37193 \u23470  (\u36275 \u23569 \u38512 \u33102 \u32147 )'\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25100 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u25100 \u23470  (\u25163 \u21413 \u38512 \u24515 \u21253 \u32147 )'\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20133 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u20133 \u23470  (\u25163 \u23569 \u38525 \u19977 \u28966 \u32147 )'\cf4 \cb1 \strokec4 \
\cb3         \}\cb1 \
\
\cb3         tcm_star_descriptions \cf2 \strokec2 =\cf4 \strokec4  \{\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u32043 \u24494 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u33086 \u32963 \u20013 \u28966 \u22303 \u27166 \u65292 \u20027 \u32113 \u25885 \u33287 \u38936 \u23566  (\u24605 \u24942 \u36942 \u37325 \u26131 \u33086 \u34395 \u28629 \u38459 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22825 \u27231 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u33213 \u32147 \u12289 \u31070 \u32147 \u33287 \u22235 \u32930 \u65292 \u20027 \u38728 \u21205 \u24605 \u32173  (\u27683 \u27231 \u26131 \u21319 \u30332 \u36942 \u24230 \u33268 \u32925 \u39080 \u22833 \u30496 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22826 \u38525 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u24515 \u12289 \u23567 \u33144 \u33287 \u38754 \u37096 \u65292 \u20027 \u20809 \u26126 \u28331 \u29030  (\u24515 \u31070 \u26131 \u20130 \u65292 \u36942 \u26106 \u21063 \u24515 \u28779 \u19978 \u28814 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u27494 \u26354 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u32954 \u12289 \u22823 \u33144 \u33287 \u31563 \u39592 \u65292 \u20027 \u32901 \u38477 \u21083 \u27589  (\u27683 \u27231 \u25910 \u25986 \u36942 \u29467 \u33268 \u33016 \u24758 \u31563 \u39592 \u20725 \u30828 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22825 \u21516 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u27700 \u36947 \u12289 \u19977 \u28966 \u33287 \u27941 \u28082 \u65292 \u20027 \u28331 \u28516 \u31119 \u27683  (\u22833 \u35519 \u26131 \u29983 \u30192 \u28629 \u27700 \u39154 \u20195 \u35613 \u36978 \u32233 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u24265 \u35998 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u24515 \u21253 \u32097 \u33287 \u34880 \u20998 \u65292 \u20027 \u34880 \u29105 \u21083 \u28872  (\u24515 \u31070 \u26131 \u24758 \u22622 \u21270 \u28779 \u65292 \u33258 \u24459 \u31070 \u32147 \u22833 \u35519 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22825 \u24220 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u32963 \u12289 \u19977 \u28966 \u33287 \u33988 \u31309 \u33021 \u21147 \u65292 \u20027 \u24235 \u27357 \u28085 \u23481  (\u36942 \u24230 \u27785 \u31309 \u26131 \u33145 \u33081 \u30192 \u28629 \u32933 \u32982 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22826 \u38512 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u33102 \u27700 \u12289 \u38512 \u34880 \u33287 \u20839 \u20998 \u27852 \u65292 \u20027 \u26376 \u20142 \u28363 \u28516  (\u19981 \u36275 \u26131 \u34395 \u21214 \u22833 \u30496 \u34880 \u34395 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u36010 \u29436 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u32925 \u33213 \u12289 \u29983 \u27542 \u27852 \u23615 \u33287 \u31563 \u33180 \u65292 \u20027 \u27442 \u26395 \u21319 \u30332  (\u25854 \u21205 \u26178 \u26131 \u21475 \u33510 \u31563 \u33180 \u32202 \u32323 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u24040 \u38272 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u21475 \u33108 \u12289 \u21628 \u21560 \u36947 \u40655 \u33180 \u33287 \u33102 \u27700 \u65292 \u20027 \u21475 \u33292 \u27700 \u39154  (\u27683 \u36947 \u27941 \u28082 \u26131 \u38459 \u28399 \u12289 \u21693 \u21897 \u19981 \u21033 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22825 \u30456 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u33152 \u33009 \u12289 \u19977 \u28966 \u33287 \u27700 \u20998 \u35519 \u31680 \u65292 \u20027 \u21360 \u26143 \u21332 \u35519  (\u22833 \u35519 \u26131 \u27700 \u28082 \u20195 \u35613 \u22833 \u32887 \u27700 \u33131 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22825 \u26753 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u33086 \u22303 \u12289 \u32908 \u32905 \u33287 \u20813 \u30123 \u20462 \u24489 \u65292 \u20027 \u22781 \u26143 \u24199 \u34093  (\u33258 \u30290 \u21147 \u24375 \u65292 \u24118 \u26377 \u28629 \u28609 \u27784 \u37325 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u19971 \u27578 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u32954 \u33287 \u25033 \u28608 \u38450 \u34907 \u31995 \u32113 \u65292 \u20027 \u32901 \u27578 \u23559 \u26143  (\u20132 \u24863 \u31070 \u32147 \u39640 \u24373 \u65292 \u34389 \u26044 \u24613 \u24615 \u30332 \u28814 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u30772 \u36557 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u33102 \u33287 \u22823 \u33144 \u65288 \u20195 \u35613 \u24490 \u29872 \u65289 \u65292 \u20027 \u32791 \u25955 \u21127 \u28872 \u35722 \u21205  (\u33021 \u37327 \u21127 \u28872 \u28040 \u32791 \u65292 \u36942 \u24230 \u21063 \u20803 \u27683 \u22823 \u20663 )'\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u25806 \u32650 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u29022 \u12305 \u37341 \u21050 \u27171 \u30171 \u24863 \u12289 \u22806 \u20663 \u12289 \u27683 \u28399 \u34880 \u30208 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u38464 \u32645 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u29022 \u12305 \u24930 \u24615 \u38577 \u30171 \u12289 \u31998 \u32399 \u19981 \u28165 \u30340 \u38459 \u28399 \u12289 \u28629 \u30208 \u20114 \u32080 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u28779 \u26143 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u29022 \u12305 \u29105 \u37034 \u12289 \u29157 \u28779 \u12289 \u24613 \u24615 \u30332 \u28814 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u37428 \u26143 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u29022 \u12305 \u29105 \u37034 \u12289 \u29157 \u28779 \u12289 \u38577 \u24615 \u29157 \u30332 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22320 \u31354 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u29022 \u12305 \u27683 \u38519 \u12289 \u34395 \u31354 \u12289 \u33021 \u37327 \u28431 \u22833 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22320 \u21163 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u29022 \u12305 \u27683 \u38519 \u12289 \u34395 \u31354 \u12289 \u21560 \u25910 \u19981 \u33391 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u31103 \u23384 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u21513 \u12305 \u31934 \u27683 \u20805 \u30408 \u12289 \u22266 \u26412 \u22521 \u20803 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22825 \u39340 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u21513 \u12305 \u27683 \u34880 \u36939 \u34892 \u12289 \u21205 \u24907 \u27969 \u36681 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u24038 \u36628 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u21513 \u12305 \u33086 \u22303 \u20043 \u27683 \u36628 \u21161 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u21491 \u24380 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u21513 \u12305 \u33102 \u27700 \u20043 \u38512 \u28085 \u21270 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u25991 \u26124 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u21513 \u12305 \u37329 \u27683 \u12289 \u24605 \u32173 \u26781 \u29702 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u25991 \u26354 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u21513 \u12305 \u27700 \u27683 \u12289 \u24773 \u24863 \u33287 \u27941 \u28082 \u20195 \u35613 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22825 \u39745 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u21513 \u12305 \u38525 \u36020 \u20154 \u12289 \u21319 \u30332 \u20043 \u27683 '\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22825 \u37470 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u12304 \u21513 \u12305 \u38512 \u36020 \u20154 \u12289 \u28145 \u23652 \u20462 \u24489 '\cf4 \cb1 \strokec4 \
\cb3         \}\cb1 \
\
\cb3         \cf8 \strokec8 # 4. \uc0\u21629 \u36523 \u23470 \u35336 \u31639 \cf4 \cb1 \strokec4 \
\cb3         yin_index \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 2\cf4 \cb1 \strokec4 \
\cb3         month_stop_index \cf2 \strokec2 =\cf4 \strokec4  (yin_index \cf2 \strokec2 +\cf4 \strokec4  (lunar_month \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \cb1 \strokec4 \
\cb3         life_palace_index \cf2 \strokec2 =\cf4 \strokec4  (month_stop_index \cf2 \strokec2 -\cf4 \strokec4  (birth_time_index \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \cb1 \strokec4 \
\cb3         body_palace_index \cf2 \strokec2 =\cf4 \strokec4  (life_palace_index \cf2 \strokec2 +\cf4 \strokec4  (birth_time_index \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \cb1 \strokec4 \
\
\cb3         palace_names \cf2 \strokec2 =\cf4 \strokec4  [\cf7 \strokec7 '\uc0\u21629 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20804 \u24351 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22827 \u22971 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u23376 \u22899 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36001 \u24091 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30142 \u21380 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36983 \u31227 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20132 \u21451 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u23448 \u31103 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30000 \u23429 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u31119 \u24503 \u23470 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u29238 \u27597 \u23470 '\cf4 \strokec4 ]\cb1 \
\cb3         palace_map \cf2 \strokec2 =\cf4 \strokec4  \{\}\cb1 \
\cb3         \cf2 \strokec2 for\cf4 \strokec4  i, palace \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 enumerate\cf4 \strokec4 (palace_names):\cb1 \
\cb3             current_index \cf2 \strokec2 =\cf4 \strokec4  (life_palace_index \cf2 \strokec2 -\cf4 \strokec4  i) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \cb1 \strokec4 \
\cb3             branch_name \cf2 \strokec2 =\cf4 \strokec4  branches[current_index]\cb1 \
\cb3             \cf2 \strokec2 if\cf4 \strokec4  branch_name \cf2 \strokec2 not\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  palace_map:\cb1 \
\cb3                 palace_map[branch_name] \cf2 \strokec2 =\cf4 \strokec4  []\cb1 \
\cb3             palace_map[branch_name].append(palace)\cb1 \
\
\cb3         \cf8 \strokec8 # 5. \uc0\u20116 \u34892 \u23616 \u33287 \u26143 \u26332 \u35336 \u31639 \cf4 \cb1 \strokec4 \
\cb3         heavenly_stems \cf2 \strokec2 =\cf4 \strokec4  [\cf7 \strokec7 '\uc0\u30002 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20057 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19993 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19969 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25098 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24049 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24218 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36763 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22764 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30328 '\cf4 \strokec4 ]\cb1 \
\cb3         year_gan \cf2 \strokec2 =\cf4 \strokec4  lunar.\cf6 \strokec6 getYearInGanZhi\cf4 \strokec4 ()[\cf9 \strokec9 0\cf4 \strokec4 ]\cb1 \
\cb3         tiger_start_gan \cf2 \strokec2 =\cf4 \strokec4  \{\cf7 \strokec7 '\uc0\u30002 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u19993 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24049 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u19993 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20057 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u25098 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24218 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u25098 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19993 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u24218 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36763 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u24218 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19969 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u22764 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22764 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u22764 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25098 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u30002 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30328 '\cf4 \strokec4 : \cf7 \strokec7 '\uc0\u30002 '\cf4 \strokec4 \}\cb1 \
\cb3         start_gan \cf2 \strokec2 =\cf4 \strokec4  tiger_start_gan.\cf6 \strokec6 get\cf4 \strokec4 (year_gan)\cb1 \
\cb3         start_gan_index \cf2 \strokec2 =\cf4 \strokec4  heavenly_stems.\cf6 \strokec6 index\cf4 \strokec4 (start_gan)\cb1 \
\cb3         steps_from_yin \cf2 \strokec2 =\cf4 \strokec4  (life_palace_index \cf2 \strokec2 -\cf4 \strokec4  yin_index) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \cb1 \strokec4 \
\cb3         life_palace_gan_index \cf2 \strokec2 =\cf4 \strokec4  (start_gan_index \cf2 \strokec2 +\cf4 \strokec4  steps_from_yin) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 10\cf4 \cb1 \strokec4 \
\cb3         life_palace_gan \cf2 \strokec2 =\cf4 \strokec4  heavenly_stems[life_palace_gan_index]\cb1 \
\cb3         life_palace_ganzhi \cf2 \strokec2 =\cf4 \strokec4  life_palace_gan \cf2 \strokec2 +\cf4 \strokec4  branches[life_palace_index]\cb1 \
\
\cb3         \cf2 \strokec2 def\cf4 \strokec4  \cf6 \strokec6 get_nayin_bureau\cf4 \strokec4 (\cf5 \strokec5 ganzhi_str\cf4 \strokec4 ):\cb1 \
\cb3             wood_zu_jue \cf2 \strokec2 =\cf4 \strokec4  [\cf7 \strokec7 '\uc0\u30002 \u23376 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20057 \u19985 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25098 \u36784 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24049 \u24051 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24218 \u23493 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36763 \u21359 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22764 \u21320 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30328 \u26410 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24218 \u30003 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36763 \u37193 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25098 \u25100 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24049 \u20133 '\cf4 \strokec4 ]\cb1 \
\cb3             water_zu_jue \cf2 \strokec2 =\cf4 \strokec4  [\cf7 \strokec7 '\uc0\u19993 \u23376 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19969 \u19985 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30002 \u23493 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20057 \u21359 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22764 \u36784 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30328 \u24051 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19993 \u21320 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19969 \u26410 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30002 \u30003 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20057 \u37193 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25098 \u23376 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24049 \u19985 '\cf4 \strokec4 ]\cb1 \
\cb3             metal_zu_jue \cf2 \strokec2 =\cf4 \strokec4  [\cf7 \strokec7 '\uc0\u22764 \u30003 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30328 \u37193 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24218 \u36784 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36763 \u24051 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30002 \u21320 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20057 \u26410 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22764 \u23493 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30328 \u21359 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24218 \u25100 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36763 \u20133 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19993 \u36784 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19969 \u24051 '\cf4 \strokec4 ]\cb1 \
\cb3             earth_zu_jue \cf2 \strokec2 =\cf4 \strokec4  [\cf7 \strokec7 '\uc0\u19993 \u36784 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19969 \u24051 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24218 \u21320 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36763 \u26410 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25098 \u30003 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24049 \u37193 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19993 \u25100 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19969 \u20133 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24218 \u23376 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36763 \u19985 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25098 \u23493 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24049 \u21359 '\cf4 \strokec4 ]\cb1 \
\cb3             \cf2 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 ganzhi_str\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  wood_zu_jue: \cf2 \strokec2 return\cf4 \strokec4  \cf7 \strokec7 "\uc0\u26408 \u19977 \u23616 "\cf4 \strokec4 , \cf9 \strokec9 3\cf4 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 elif\cf4 \strokec4  \cf5 \strokec5 ganzhi_str\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  water_zu_jue: \cf2 \strokec2 return\cf4 \strokec4  \cf7 \strokec7 "\uc0\u27700 \u20108 \u23616 "\cf4 \strokec4 , \cf9 \strokec9 2\cf4 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 elif\cf4 \strokec4  \cf5 \strokec5 ganzhi_str\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  metal_zu_jue: \cf2 \strokec2 return\cf4 \strokec4  \cf7 \strokec7 "\uc0\u37329 \u22235 \u23616 "\cf4 \strokec4 , \cf9 \strokec9 4\cf4 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 elif\cf4 \strokec4  \cf5 \strokec5 ganzhi_str\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  earth_zu_jue: \cf2 \strokec2 return\cf4 \strokec4  \cf7 \strokec7 "\uc0\u22303 \u20116 \u23616 "\cf4 \strokec4 , \cf9 \strokec9 5\cf4 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 else\cf4 \strokec4 : \cf2 \strokec2 return\cf4 \strokec4  \cf7 \strokec7 "\uc0\u28779 \u20845 \u23616 "\cf4 \strokec4 , \cf9 \strokec9 6\cf4 \cb1 \strokec4 \
\
\cb3         bureau_name, bureau_number \cf2 \strokec2 =\cf4 \strokec4  \cf6 \strokec6 get_nayin_bureau\cf4 \strokec4 (life_palace_ganzhi)\cb1 \
\cb3         lunar_day \cf2 \strokec2 =\cf4 \strokec4  lunar.\cf6 \strokec6 getDay\cf4 \strokec4 ()\cb1 \
\cb3         bureau_num \cf2 \strokec2 =\cf4 \strokec4  bureau_number\cb1 \
\
\cb3         remainder \cf2 \strokec2 =\cf4 \strokec4  lunar_day \cf2 \strokec2 %\cf4 \strokec4  bureau_num\cb1 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  remainder \cf2 \strokec2 ==\cf4 \strokec4  \cf9 \strokec9 0\cf4 \strokec4 :\cb1 \
\cb3             ziwei_index \cf2 \strokec2 =\cf4 \strokec4  (yin_index \cf2 \strokec2 +\cf4 \strokec4  ((lunar_day \cf2 \strokec2 //\cf4 \strokec4  bureau_num) \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 else\cf4 \strokec4 :\cb1 \
\cb3             complement \cf2 \strokec2 =\cf4 \strokec4  bureau_num \cf2 \strokec2 -\cf4 \strokec4  remainder\cb1 \
\cb3             adjusted_day \cf2 \strokec2 =\cf4 \strokec4  lunar_day \cf2 \strokec2 +\cf4 \strokec4  complement\cb1 \
\cb3             quotient \cf2 \strokec2 =\cf4 \strokec4  adjusted_day \cf2 \strokec2 //\cf4 \strokec4  bureau_num\cb1 \
\cb3             \cf2 \strokec2 if\cf4 \strokec4  complement \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 2\cf4 \strokec4  \cf2 \strokec2 !=\cf4 \strokec4  \cf9 \strokec9 0\cf4 \strokec4 :\cb1 \
\cb3                 ziwei_index \cf2 \strokec2 =\cf4 \strokec4  (yin_index \cf2 \strokec2 +\cf4 \strokec4  (quotient \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 ) \cf2 \strokec2 -\cf4 \strokec4  complement) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 else\cf4 \strokec4 :\cb1 \
\cb3                 ziwei_index \cf2 \strokec2 =\cf4 \strokec4  (yin_index \cf2 \strokec2 +\cf4 \strokec4  (quotient \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 ) \cf2 \strokec2 +\cf4 \strokec4  complement) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \cb1 \strokec4 \
\
\cb3         tianfu_index \cf2 \strokec2 =\cf4 \strokec4  (\cf9 \strokec9 4\cf4 \strokec4  \cf2 \strokec2 -\cf4 \strokec4  ziwei_index) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \cb1 \strokec4 \
\
\cb3         ziwei_group \cf2 \strokec2 =\cf4 \strokec4  [(\cf7 \strokec7 '\uc0\u32043 \u24494 '\cf4 \strokec4 , \cf9 \strokec9 0\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u22825 \u27231 '\cf4 \strokec4 , \cf9 \strokec9 -1\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u22826 \u38525 '\cf4 \strokec4 , \cf9 \strokec9 -3\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u27494 \u26354 '\cf4 \strokec4 , \cf9 \strokec9 -4\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u22825 \u21516 '\cf4 \strokec4 , \cf9 \strokec9 -5\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u24265 \u35998 '\cf4 \strokec4 , \cf9 \strokec9 -8\cf4 \strokec4 )]\cb1 \
\cb3         tianfu_group \cf2 \strokec2 =\cf4 \strokec4  [(\cf7 \strokec7 '\uc0\u22825 \u24220 '\cf4 \strokec4 , \cf9 \strokec9 0\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u22826 \u38512 '\cf4 \strokec4 , \cf9 \strokec9 1\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u36010 \u29436 '\cf4 \strokec4 , \cf9 \strokec9 2\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u24040 \u38272 '\cf4 \strokec4 , \cf9 \strokec9 3\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u22825 \u30456 '\cf4 \strokec4 , \cf9 \strokec9 4\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u22825 \u26753 '\cf4 \strokec4 , \cf9 \strokec9 5\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u19971 \u27578 '\cf4 \strokec4 , \cf9 \strokec9 6\cf4 \strokec4 ), (\cf7 \strokec7 '\uc0\u30772 \u36557 '\cf4 \strokec4 , \cf9 \strokec9 8\cf4 \strokec4 )]\cb1 \
\
\cb3         star_map \cf2 \strokec2 =\cf4 \strokec4  \{i: [] \cf2 \strokec2 for\cf4 \strokec4  i \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 range\cf4 \strokec4 (\cf9 \strokec9 12\cf4 \strokec4 )\}\cb1 \
\cb3         \cf2 \strokec2 for\cf4 \strokec4  star_name, offset \cf2 \strokec2 in\cf4 \strokec4  ziwei_group:\cb1 \
\cb3             star_map[(ziwei_index \cf2 \strokec2 +\cf4 \strokec4  offset) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (star_name)\cb1 \
\cb3         \cf2 \strokec2 for\cf4 \strokec4  star_name, offset \cf2 \strokec2 in\cf4 \strokec4  tianfu_group:\cb1 \
\cb3             star_map[(tianfu_index \cf2 \strokec2 +\cf4 \strokec4  offset) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (star_name)\cb1 \
\
\cb3         \cf8 \strokec8 # \uc0\u36628 \u20304 \u29022 \u26332 \cf4 \cb1 \strokec4 \
\cb3         star_map[(\cf9 \strokec9 3\cf4 \strokec4  \cf2 \strokec2 +\cf4 \strokec4  (lunar_month \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u24038 \u36628 '\cf4 \strokec4 )\cb1 \
\cb3         star_map[(\cf9 \strokec9 9\cf4 \strokec4  \cf2 \strokec2 -\cf4 \strokec4  (lunar_month \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u21491 \u24380 '\cf4 \strokec4 )\cb1 \
\cb3         star_map[(\cf9 \strokec9 9\cf4 \strokec4  \cf2 \strokec2 -\cf4 \strokec4  (birth_time_index \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u25991 \u26124 '\cf4 \strokec4 )\cb1 \
\cb3         star_map[(\cf9 \strokec9 3\cf4 \strokec4  \cf2 \strokec2 +\cf4 \strokec4  (birth_time_index \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u25991 \u26354 '\cf4 \strokec4 )\cb1 \
\
\cb3         tiankui_tianyue_map \cf2 \strokec2 =\cf4 \strokec4  \{\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u30002 '\cf4 \strokec4 : (\cf9 \strokec9 1\cf4 \strokec4 , \cf9 \strokec9 7\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u25098 '\cf4 \strokec4 : (\cf9 \strokec9 1\cf4 \strokec4 , \cf9 \strokec9 7\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u24218 '\cf4 \strokec4 : (\cf9 \strokec9 1\cf4 \strokec4 , \cf9 \strokec9 7\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u20057 '\cf4 \strokec4 : (\cf9 \strokec9 0\cf4 \strokec4 , \cf9 \strokec9 8\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u24049 '\cf4 \strokec4 : (\cf9 \strokec9 0\cf4 \strokec4 , \cf9 \strokec9 8\cf4 \strokec4 ),\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u19993 '\cf4 \strokec4 : (\cf9 \strokec9 11\cf4 \strokec4 , \cf9 \strokec9 9\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u19969 '\cf4 \strokec4 : (\cf9 \strokec9 11\cf4 \strokec4 , \cf9 \strokec9 9\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u22764 '\cf4 \strokec4 : (\cf9 \strokec9 3\cf4 \strokec4 , \cf9 \strokec9 5\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u30328 '\cf4 \strokec4 : (\cf9 \strokec9 3\cf4 \strokec4 , \cf9 \strokec9 5\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u36763 '\cf4 \strokec4 : (\cf9 \strokec9 6\cf4 \strokec4 , \cf9 \strokec9 2\cf4 \strokec4 )\cb1 \
\cb3         \}\cb1 \
\cb3         kui, yue \cf2 \strokec2 =\cf4 \strokec4  tiankui_tianyue_map.\cf6 \strokec6 get\cf4 \strokec4 (year_gan, (\cf9 \strokec9 1\cf4 \strokec4 , \cf9 \strokec9 7\cf4 \strokec4 ))\cb1 \
\cb3         star_map[kui].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u22825 \u39745 '\cf4 \strokec4 )\cb1 \
\cb3         star_map[yue].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u22825 \u37470 '\cf4 \strokec4 )\cb1 \
\
\cb3         lucun_map \cf2 \strokec2 =\cf4 \strokec4  \{\cf7 \strokec7 '\uc0\u30002 '\cf4 \strokec4 : \cf9 \strokec9 2\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20057 '\cf4 \strokec4 : \cf9 \strokec9 3\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19993 '\cf4 \strokec4 : \cf9 \strokec9 5\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19969 '\cf4 \strokec4 : \cf9 \strokec9 6\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25098 '\cf4 \strokec4 : \cf9 \strokec9 5\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24049 '\cf4 \strokec4 : \cf9 \strokec9 6\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24218 '\cf4 \strokec4 : \cf9 \strokec9 8\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36763 '\cf4 \strokec4 : \cf9 \strokec9 9\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22764 '\cf4 \strokec4 : \cf9 \strokec9 11\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30328 '\cf4 \strokec4 : \cf9 \strokec9 0\cf4 \strokec4 \}\cb1 \
\cb3         lucun_pos \cf2 \strokec2 =\cf4 \strokec4  lucun_map.\cf6 \strokec6 get\cf4 \strokec4 (year_gan, \cf9 \strokec9 2\cf4 \strokec4 )\cb1 \
\cb3         star_map[lucun_pos].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u31103 \u23384 '\cf4 \strokec4 )\cb1 \
\cb3         star_map[(lucun_pos \cf2 \strokec2 +\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 ) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u25806 \u32650 '\cf4 \strokec4 )\cb1 \
\cb3         star_map[(lucun_pos \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 ) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u38464 \u32645 '\cf4 \strokec4 )\cb1 \
\
\cb3         year_zhi \cf2 \strokec2 =\cf4 \strokec4  lunar.\cf6 \strokec6 getYearInGanZhi\cf4 \strokec4 ()[\cf9 \strokec9 1\cf4 \strokec4 ]\cb1 \
\cb3         hx_start \cf2 \strokec2 =\cf4 \strokec4  \{\cf7 \strokec7 '\uc0\u23493 '\cf4 \strokec4 : \cf9 \strokec9 1\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u21320 '\cf4 \strokec4 : \cf9 \strokec9 1\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25100 '\cf4 \strokec4 : \cf9 \strokec9 1\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30003 '\cf4 \strokec4 : \cf9 \strokec9 2\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u23376 '\cf4 \strokec4 : \cf9 \strokec9 2\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36784 '\cf4 \strokec4 : \cf9 \strokec9 2\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24051 '\cf4 \strokec4 : \cf9 \strokec9 3\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u37193 '\cf4 \strokec4 : \cf9 \strokec9 3\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19985 '\cf4 \strokec4 : \cf9 \strokec9 3\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20133 '\cf4 \strokec4 : \cf9 \strokec9 9\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u21359 '\cf4 \strokec4 : \cf9 \strokec9 9\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u26410 '\cf4 \strokec4 : \cf9 \strokec9 9\cf4 \strokec4 \}.\cf6 \strokec6 get\cf4 \strokec4 (year_zhi, \cf9 \strokec9 1\cf4 \strokec4 )\cb1 \
\cb3         lx_start \cf2 \strokec2 =\cf4 \strokec4  \{\cf7 \strokec7 '\uc0\u23493 '\cf4 \strokec4 : \cf9 \strokec9 3\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u21320 '\cf4 \strokec4 : \cf9 \strokec9 3\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25100 '\cf4 \strokec4 : \cf9 \strokec9 3\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30003 '\cf4 \strokec4 : \cf9 \strokec9 10\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u23376 '\cf4 \strokec4 : \cf9 \strokec9 10\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36784 '\cf4 \strokec4 : \cf9 \strokec9 10\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24051 '\cf4 \strokec4 : \cf9 \strokec9 11\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u37193 '\cf4 \strokec4 : \cf9 \strokec9 11\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u19985 '\cf4 \strokec4 : \cf9 \strokec9 11\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u20133 '\cf4 \strokec4 : \cf9 \strokec9 10\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u21359 '\cf4 \strokec4 : \cf9 \strokec9 10\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u26410 '\cf4 \strokec4 : \cf9 \strokec9 10\cf4 \strokec4 \}.\cf6 \strokec6 get\cf4 \strokec4 (year_zhi, \cf9 \strokec9 3\cf4 \strokec4 )\cb1 \
\cb3         star_map[(hx_start \cf2 \strokec2 +\cf4 \strokec4  (birth_time_index \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u28779 \u26143 '\cf4 \strokec4 )\cb1 \
\cb3         star_map[(lx_start \cf2 \strokec2 +\cf4 \strokec4  (birth_time_index \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u37428 \u26143 '\cf4 \strokec4 )\cb1 \
\
\cb3         star_map[(\cf9 \strokec9 11\cf4 \strokec4  \cf2 \strokec2 -\cf4 \strokec4  (birth_time_index \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u22320 \u31354 '\cf4 \strokec4 )\cb1 \
\cb3         star_map[(\cf9 \strokec9 11\cf4 \strokec4  \cf2 \strokec2 +\cf4 \strokec4  (birth_time_index \cf2 \strokec2 -\cf4 \strokec4  \cf9 \strokec9 1\cf4 \strokec4 )) \cf2 \strokec2 %\cf4 \strokec4  \cf9 \strokec9 12\cf4 \strokec4 ].\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 '\uc0\u22320 \u21163 '\cf4 \strokec4 )\cb1 \
\
\cb3         \cf8 \strokec8 # \uc0\u22235 \u21270 \cf4 \cb1 \strokec4 \
\cb3         birth_hua \cf2 \strokec2 =\cf4 \strokec4  \{\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u30002 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u24265 \u35998 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u30772 \u36557 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u27494 \u26354 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22826 \u38525 '\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u20057 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u22825 \u27231 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22825 \u26753 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u32043 \u24494 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22826 \u38512 '\cf4 \strokec4 ),\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u19993 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u22825 \u21516 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22825 \u27231 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25991 \u26124 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24265 \u35998 '\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u19969 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u22826 \u38512 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22825 \u21516 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22825 \u27231 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24040 \u38272 '\cf4 \strokec4 ),\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u25098 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u36010 \u29436 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22826 \u38512 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u21491 \u24380 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22825 \u27231 '\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u24049 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u27494 \u26354 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36010 \u29436 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22825 \u26753 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25991 \u26354 '\cf4 \strokec4 ),\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u24218 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u22826 \u38525 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u27494 \u26354 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22826 \u38512 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22825 \u21516 '\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u36763 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u24040 \u38272 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22826 \u38525 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25991 \u26354 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u25991 \u26124 '\cf4 \strokec4 ),\cb1 \
\cb3             \cf7 \strokec7 '\uc0\u22764 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u22825 \u26753 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u32043 \u24494 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24038 \u36628 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22825 \u27231 '\cf4 \strokec4 ), \cf7 \strokec7 '\uc0\u30328 '\cf4 \strokec4 : (\cf7 \strokec7 '\uc0\u30772 \u36557 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u24040 \u38272 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u22826 \u38512 '\cf4 \strokec4 , \cf7 \strokec7 '\uc0\u36010 \u29436 '\cf4 \strokec4 )\cb1 \
\cb3         \}\cb1 \
\cb3         lu, quan, ke, ji \cf2 \strokec2 =\cf4 \strokec4  birth_hua.\cf6 \strokec6 get\cf4 \strokec4 (year_gan, (\cf7 \strokec7 ''\cf4 \strokec4 , \cf7 \strokec7 ''\cf4 \strokec4 , \cf7 \strokec7 ''\cf4 \strokec4 , \cf7 \strokec7 ''\cf4 \strokec4 ))\cb1 \
\
\cb3         \cf2 \strokec2 for\cf4 \strokec4  pos \cf2 \strokec2 in\cf4 \strokec4  star_map:\cb1 \
\cb3             updated_stars \cf2 \strokec2 =\cf4 \strokec4  []\cb1 \
\cb3             \cf2 \strokec2 for\cf4 \strokec4  star \cf2 \strokec2 in\cf4 \strokec4  star_map[pos]:\cb1 \
\cb3                 \cf2 \strokec2 if\cf4 \strokec4  star \cf2 \strokec2 ==\cf4 \strokec4  lu: updated_stars.\cf6 \strokec6 append\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\cf2 \strokec2 \{\cf4 \strokec4 star\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u12304 \u21270 \u31103 \u12305 "\cf4 \strokec4 )\cb1 \
\cb3                 \cf2 \strokec2 elif\cf4 \strokec4  star \cf2 \strokec2 ==\cf4 \strokec4  quan: updated_stars.\cf6 \strokec6 append\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\cf2 \strokec2 \{\cf4 \strokec4 star\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u12304 \u21270 \u27402 \u12305 "\cf4 \strokec4 )\cb1 \
\cb3                 \cf2 \strokec2 elif\cf4 \strokec4  star \cf2 \strokec2 ==\cf4 \strokec4  ke: updated_stars.\cf6 \strokec6 append\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\cf2 \strokec2 \{\cf4 \strokec4 star\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u12304 \u21270 \u31185 \u12305 "\cf4 \strokec4 )\cb1 \
\cb3                 \cf2 \strokec2 elif\cf4 \strokec4  star \cf2 \strokec2 ==\cf4 \strokec4  ji: updated_stars.\cf6 \strokec6 append\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\cf2 \strokec2 \{\cf4 \strokec4 star\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u12304 \u21270 \u24524 \u12305 "\cf4 \strokec4 )\cb1 \
\cb3                 \cf2 \strokec2 else\cf4 \strokec4 : updated_stars.\cf6 \strokec6 append\cf4 \strokec4 (star)\cb1 \
\cb3             star_map[pos] \cf2 \strokec2 =\cf4 \strokec4  updated_stars\cb1 \
\
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .subheader(\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u12304 \u20116 \u34892 \u23616 \u12305 \u65306 \cf2 \strokec2 \{\cf4 \strokec4 bureau_name\cf2 \strokec2 \}\cf7 \strokec7  (\uc0\u29983 \u24180 \u24178 \u65306 \cf2 \strokec2 \{\cf4 \strokec4 year_gan\cf2 \strokec2 \}\cf7 \strokec7 )"\cf4 \strokec4 )\cb1 \
\
\cb3         \cf8 \strokec8 # 6. \uc0\u32178 \u38913 \u21576 \u29694 \u32080 \u26524 \cf4 \cb1 \strokec4 \
\cb3         chart_summary \cf2 \strokec2 =\cf4 \strokec4  []\cb1 \
\cb3         \cf2 \strokec2 for\cf4 \strokec4  i, branch \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 enumerate\cf4 \strokec4 (branches):\cb1 \
\cb3             palaces \cf2 \strokec2 =\cf4 \strokec4  palace_map.\cf6 \strokec6 get\cf4 \strokec4 (branch, [])\cb1 \
\cb3             palace_str \cf2 \strokec2 =\cf4 \strokec4  \cf7 \strokec7 ', '\cf4 \strokec4 .\cf6 \strokec6 join\cf4 \strokec4 (palaces) \cf2 \strokec2 if\cf4 \strokec4  palaces \cf2 \strokec2 else\cf4 \strokec4  \cf7 \strokec7 "\uc0\u65288 \u28961 \u20027 \u23470 \u65289 "\cf4 \cb1 \strokec4 \
\cb3             stars \cf2 \strokec2 =\cf4 \strokec4  star_map.\cf6 \strokec6 get\cf4 \strokec4 (i, [])\cb1 \
\cb3             \cb1 \
\cb3             tags \cf2 \strokec2 =\cf4 \strokec4  []\cb1 \
\cb3             \cf2 \strokec2 if\cf4 \strokec4  i \cf2 \strokec2 ==\cf4 \strokec4  life_palace_index: tags.\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u9733  \u21629 \u23470 "\cf4 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 if\cf4 \strokec4  i \cf2 \strokec2 ==\cf4 \strokec4  body_palace_index: tags.\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u9670  \u36523 \u23470 "\cf4 \strokec4 )\cb1 \
\cb3             tag_str \cf2 \strokec2 =\cf4 \strokec4  \cf2 \strokec2 f\cf7 \strokec7 "  [\cf2 \strokec2 \{\cf7 \strokec7 ' '\cf4 \strokec4 .\cf6 \strokec6 join\cf4 \strokec4 (tags)\cf2 \strokec2 \}\cf7 \strokec7 ]"\cf4 \strokec4  \cf2 \strokec2 if\cf4 \strokec4  tags \cf2 \strokec2 else\cf4 \strokec4  \cf7 \strokec7 ""\cf4 \cb1 \strokec4 \
\cb3             \cb1 \
\cb3             organ_str \cf2 \strokec2 =\cf4 \strokec4  branch_to_organ.\cf6 \strokec6 get\cf4 \strokec4 (branch, branch)\cb1 \
\cb3             \cb1 \
\cb3             star_details \cf2 \strokec2 =\cf4 \strokec4  []\cb1 \
\cb3             \cf2 \strokec2 with\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .expander(\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u12304 \cf2 \strokec2 \{\cf4 \strokec4 organ_str\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u12305  \cf2 \strokec2 \{\cf4 \strokec4 palace_str\cf2 \strokec2 \}\cf7 \strokec7  \cf2 \strokec2 \{\cf4 \strokec4 tag_str\cf2 \strokec2 \}\cf7 \strokec7 "\cf4 \strokec4 ):\cb1 \
\cb3                 \cf2 \strokec2 if\cf4 \strokec4  stars:\cb1 \
\cb3                     \cf2 \strokec2 for\cf4 \strokec4  star \cf2 \strokec2 in\cf4 \strokec4  stars:\cb1 \
\cb3                         clean_star \cf2 \strokec2 =\cf4 \strokec4  star.split(\cf7 \strokec7 '\uc0\u12304 '\cf4 \strokec4 )[\cf9 \strokec9 0\cf4 \strokec4 ]\cb1 \
\cb3                         desc \cf2 \strokec2 =\cf4 \strokec4  tcm_star_descriptions.\cf6 \strokec6 get\cf4 \strokec4 (clean_star, \cf7 \strokec7 '\uc0\u32147 \u32097 \u27683 \u27231 \u27969 \u36681 \u20301 \u40670 '\cf4 \strokec4 )\cb1 \
\cb3                         \cf5 \strokec5 st\cf4 \strokec4 .markdown(\cf2 \strokec2 f\cf7 \strokec7 "- **\cf2 \strokec2 \{\cf4 \strokec4 star\cf2 \strokec2 \}\cf7 \strokec7 **\uc0\u65306 \cf2 \strokec2 \{\cf4 \strokec4 desc\cf2 \strokec2 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3                         star_details.\cf6 \strokec6 append\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\cf2 \strokec2 \{\cf4 \strokec4 star\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u65306 \cf2 \strokec2 \{\cf4 \strokec4 desc\cf2 \strokec2 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\cb3                 \cf2 \strokec2 else\cf4 \strokec4 :\cb1 \
\cb3                     \cf5 \strokec5 st\cf4 \strokec4 .markdown(\cf7 \strokec7 "- *\uc0\u65288 \u26412 \u32147 \u32097 \u28961 \u20027 \u26143 \u33287 \u20027 \u35201 \u29022 \u26332 \u39376 \u23432 \u65292 \u27683 \u27231 \u24179 \u21644 \u65289 *"\cf4 \strokec4 )\cb1 \
\cb3                     star_details.\cf6 \strokec6 append\cf4 \strokec4 (\cf7 \strokec7 "\uc0\u26412 \u32147 \u32097 \u24179 \u21644 \u65292 \u28961 \u20027 \u26143 \u33287 \u20027 \u35201 \u29022 \u26332 "\cf4 \strokec4 )\cb1 \
\
\cb3             chart_summary.\cf6 \strokec6 append\cf4 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u12304 \cf2 \strokec2 \{\cf4 \strokec4 organ_str\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u12305 \u23470 \u20301 \u23660 \u24615 : \cf2 \strokec2 \{\cf4 \strokec4 palace_str\cf2 \strokec2 \}\{\cf4 \strokec4 tag_str\cf2 \strokec2 \}\cf7 \strokec7  | \uc0\u39376 \u23432 \u26143 \u26332 \u33287 \u30149 \u29702 : \cf2 \strokec2 \{\cf7 \strokec7 ', '\cf4 \strokec4 .\cf6 \strokec6 join\cf4 \strokec4 (star_details)\cf2 \strokec2 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\
\cb3         \cf8 \strokec8 # ==========================================\cf4 \cb1 \strokec4 \
\cb3         \cf8 \strokec8 # 7. AI \uc0\u26234 \u24935 \u20013 \u37291 \u32147 \u32097 \u21629 \u29702 \u25972 \u39636 \u35299 \u35712 \cf4 \cb1 \strokec4 \
\cb3         \cf8 \strokec8 # ==========================================\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .markdown(\cf7 \strokec7 "---"\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .subheader(\cf7 \strokec7 "\uc0\u55358 \u56598  AI \u26234 \u24935 \u20013 \u37291 \u32147 \u32097 \u21629 \u29702 \u25972 \u39636 \u35299 \u35712 "\cf4 \strokec4 )\cb1 \
\cb3         user_question \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .text_input(\cf7 \strokec7 "\uc0\u20320 \u24819 \u29305 \u21029 \u35531 \u25945  AI \u20160 \u40636 \u26041 \u21521 \u65311 "\cf4 \strokec4 , \cf5 \strokec5 value\cf2 \strokec2 =\cf7 \strokec7 "\uc0\u35531 \u37341 \u23565 \u36889 \u24373 \u32147 \u32097 \u21629 \u30436 \u36914 \u34892 \u25972 \u39636 \u36523 \u24515 \u27683 \u27231 \u33287 \u39636 \u36074 \u20670 \u21521 \u30340 \u28145 \u24230 \u32156 \u21512 \u20998 \u26512 "\cf4 \strokec4 )\cb1 \
\
\cb3         \cf2 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .button(\cf7 \strokec7 "\uc0\u55357 \u56622  \u35531  AI \u36914 \u34892 \u33256 \u24202 \u20013 \u37291 \u32147 \u32097 \u32156 \u21512 \u35299 \u35712 "\cf4 \strokec4 , \cf5 \strokec5 type\cf2 \strokec2 =\cf7 \strokec7 "primary"\cf4 \strokec4 ):\cb1 \
\cb3             \cf2 \strokec2 with\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .spinner(\cf7 \strokec7 "AI \uc0\u27491 \u22312 \u32080 \u21512 \u32043 \u24494 \u26143 \u35937 \u33287 \u20013 \u37291 \u32147 \u32097 \u23416 \u29702 \u65292 \u28858 \u24744 \u28145 \u24230 \u35299 \u26512 \u20013 ..."\cf4 \strokec4 ):\cb1 \
\cb3                 full_chart_text \cf2 \strokec2 =\cf4 \strokec4  \cf7 \strokec7 "\cf2 \strokec2 \\n\cf7 \strokec7 "\cf4 \strokec4 .\cf6 \strokec6 join\cf4 \strokec4 (chart_summary)\cb1 \
\cb3                 prompt \cf2 \strokec2 =\cf4 \strokec4  \cf2 \strokec2 f\cf7 \strokec7 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7                 \uc0\u20320 \u26159 \u19968 \u20301 \u34701 \u21512 \u20102 \u12300 \u20659 \u32113 \u32043 \u24494 \u26007 \u25976 \u35937 \u25976 \u25512 \u28436 \u12301 \u33287 \u12300 \u20013 \u37291 \u23416 \u29702 \u12289 \u32147 \u32097 \u27683 \u27231 \u12289 \u36523 \u24515 \u30149 \u27231 \u12301 \u30340 \u38914 \u23574 \u20013 \u37291 \u24107 \u33287 \u21629 \u29702 \u23560 \u23478 \u12290 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \uc0\u29694 \u22312 \u26377 \u19968 \u20301 \u20351 \u29992 \u32773 \u30340 \u32043 \u24494 \u26007 \u25976 \u32147 \u32097 \u21629 \u30436 \u25976 \u25818 \u22914 \u19979 \u65306 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \uc0\u12304 \u22522 \u26412 \u29983 \u36784 \u12305 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \uc0\u29983 \u24180 \u24178 \u25903 \u65306 \cf2 \strokec2 \{\cf4 \strokec4 year_gan\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u24180  | \u20116 \u34892 \u23616 \u65306 \cf2 \strokec2 \{\cf4 \strokec4 bureau_name\cf2 \strokec2 \}\cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \uc0\u21629 \u23470 \u20301 \u32622 \u65306 \cf2 \strokec2 \{\cf4 \strokec4 branches[life_palace_index]\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u23470  | \u36523 \u23470 \u20301 \u32622 \u65306 \cf2 \strokec2 \{\cf4 \strokec4 branches[body_palace_index]\cf2 \strokec2 \}\cf7 \strokec7 \uc0\u23470 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \uc0\u12304 \u21313 \u20108 \u32147 \u32097 \u33287 \u26143 \u26332 \u30149 \u29702 \u20998 \u20296 \u12305 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \cf2 \strokec2 \{\cf4 \strokec4 full_chart_text\cf2 \strokec2 \}\cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \uc0\u12304 \u20351 \u29992 \u32773 \u30340 \u25552 \u21839 \u25110 \u38364 \u27880 \u40670 \u12305 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \cf2 \strokec2 \{\cf4 \strokec4 user_question\cf2 \strokec2 \}\cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \uc0\u35531 \u26681 \u25818 \u20197 \u19978 \u25976 \u25818 \u65292 \u20197 \u23560 \u26989 \u12289 \u28331 \u26262 \u19988 \u20855 \u33256 \u24202 \u27934 \u23519 \u21147 \u30340 \u35486 \u27683 \u65292 \u25552 \u20379 \u19968 \u20221 \u32080 \u27083 \u21270 \u30340 \u25972 \u39636 \u35299 \u35712 \u22577 \u21578 \u65292 \u21253 \u21547 \u65306 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 1. **\uc0\u20808 \u22825 \u39636 \u36074 \u33287 \u27683 \u27231 \u27166 \u32016 \u20998 \u26512 **\u65288 \u32080 \u21512 \u21629 \u36523 \u23470 \u33287 \u20116 \u34892 \u23616 \u30340 \u25972 \u39636 \u27683 \u34880 \u29305 \u36074 \u65289 \u12290 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 2. **\uc0\u26680 \u24515 \u30149 \u29702 \u33287 \u32147 \u32097 \u21345 \u40670 **\u65288 \u29305 \u21029 \u25351 \u20986 \u21463 \u29022 \u26332 \u25110 \u21270 \u24524 \u24433 \u38911 \u12289 \u23481 \u26131 \u20986 \u29694 \u21151 \u33021 \u22833 \u35519 \u30340 \u32147 \u32097 \u33287 \u33247 \u33105 \u65289 \u12290 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 3. **\uc0\u36523 \u24515 \u20114 \u21205 \u33287 \u28507 \u22312 \u20670 \u21521 **\u65288 \u26143 \u26332 \u35937 \u25976 \u22914 \u20309 \u23565 \u25033 \u21040 \u24773 \u32210 \u12289 \u22739 \u21147 \u27169 \u24335 \u25110 \u29983 \u29702 \u34920 \u29694 \u65289 \u12290 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 4. **\uc0\u26085 \u24120 \u20013 \u37291 \u39178 \u29983 \u33287 \u35519 \u29702 \u24314 \u35696 **\u65288 \u39154 \u39135 \u12289 \u20316 \u24687 \u12289 \u24773 \u24535 \u35519 \u31680 \u31561 \u20855 \u39636 \u26041 \u21521 \u65289 \u12290 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 \uc0\u35531 \u20351 \u29992 \u32321 \u39636 \u20013 \u25991 \u22238 \u31572 \u65292 \u25490 \u29256 \u28165 \u26224 \u26131 \u35712 \u12290 \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7                 """\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3                 api_key \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 st\cf4 \strokec4 .secrets[\cf7 \strokec7 "GEMINI_API_KEY"\cf4 \strokec4 ]\cb1 \
\cb3                 client \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 genai\cf4 \strokec4 .\cf5 \strokec5 Client\cf4 \strokec4 (\cf5 \strokec5 api_key\cf2 \strokec2 =\cf4 \strokec4 api_key)\cb1 \
\cb3                 response \cf2 \strokec2 =\cf4 \strokec4  client.models.\cf6 \strokec6 generate_content\cf4 \strokec4 (\cb1 \
\cb3                     \cf5 \strokec5 model\cf2 \strokec2 =\cf7 \strokec7 'gemini-2.5-flash'\cf4 \strokec4 ,\cb1 \
\cb3                     \cf5 \strokec5 contents\cf2 \strokec2 =\cf4 \strokec4 prompt\cb1 \
\cb3                 )\cb1 \
\
\cb3                 \cf5 \strokec5 st\cf4 \strokec4 .success(\cf7 \strokec7 "\uc0\u20998 \u26512 \u23436 \u25104 \u65281 "\cf4 \strokec4 )\cb1 \
\cb3                 \cf5 \strokec5 st\cf4 \strokec4 .markdown(\cf7 \strokec7 "### \uc0\u55357 \u56523  AI \u33256 \u24202 \u20013 \u37291 \u32147 \u32097 \u21629 \u29702 \u32156 \u21512 \u22577 \u21578 "\cf4 \strokec4 )\cb1 \
\cb3                 \cf5 \strokec5 st\cf4 \strokec4 .markdown(response.text)\cb1 \
\
\cb3     \cf2 \strokec2 except\cf4 \strokec4  \cf5 \strokec5 Exception\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  e:\cb1 \
\cb3         \cf5 \strokec5 st\cf4 \strokec4 .error(\cf2 \strokec2 f\cf7 \strokec7 "\uc0\u35336 \u31639 \u36942 \u31243 \u30332 \u29983 \u37679 \u35492 \u25110  API Key \u26410 \u27491 \u30906 \u35373 \u23450 \u65306 \cf2 \strokec2 \{\cf4 \strokec4 e\cf2 \strokec2 \}\cf7 \strokec7 "\cf4 \strokec4 )\cb1 \
\
}