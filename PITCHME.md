## Scipy.integrate.odeint

adams法とオイラー法の数値計算の誤差をみる。

---
Scipy.integrate.odeint : FORTRAN77

- ODEPACK
	- DLSODA
		- 9種類の常微分方程式の解法
   [Netlib](http://www.netlib.org/master_counts2.html#odepack)
   [odepack](https://www.netlib.org/odepack/index.html)

-----

ソースコードを見てみよう
	https://people.sc.fsu.edu/~jburkardt/f77_src/odepack/odepack.html
	この中にLSODAがある
		出力ファイルがリファレンスに有る
		https://people.sc.fsu.edu/~jburkardt/f77_src/odepack/odepack_prb3_output.txt

-----


ところで、どのadams法か？
	記載なし
    陽解法がいいのか？
		adams-multon-bashforce法かな

-----

- Scipy.integrate.odeint（Adams法）
- オイラー法
- 厳密解

この３つを比較してみよう

-----





-----






