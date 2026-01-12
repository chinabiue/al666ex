---
title: Markdown 数学公式支持 in VSCode
---
Markdown 的数学公式吸纳了大部分的 Latex 语法, 你可以以一种简单的方式在 VS Code 中书写数学公式.

## 1. 数学符号/字母的表示方法

### 1.1 希腊字母
| 符号                     | 格式                 | 符号                     | 格式                 |
| ------------------------ | -------------------- | ------------------------ | -------------------- |
| $\Alpha$                 | \Alpha               | $\alpha$                 | \alpha               |
| $\Beta$                  | \Beta                | $\beta$                  | \beta                |
| $\Gamma$,$\varGamma$     | \Gamma,\varGamma     | $\gamma$                 | \gamma               |
| $\Delta$,$\varDelta$     | \Delta,\varDelta     | $\delta$                 | \delta               |
| $\Epsilon$               | \Epsilon             | $\epsilon$,$\varepsilon$ | \epsilon,\varepsilon |
| $\Zeta$                  | \Zeta                | $\zeta$                  | \zeta                |
| $\Eta$                   | \Eta                 | $\eta$                   | \eta                 |
| $\Theta$,$\varTheta$     | \Theta,\varTheta     | $\theta$,$\vartheta$     | \theta,\vartheta     |
| $\Iota$                  | \Iota                | $\iota$                  | \iota                |
| $\Kappa$                 | \Kappa               | $\kappa$                 | \kappa               |
| $\Lambda$,$\varLambda$   | \Lambda,\varLambda   | $\lambda$                | \lambda              |
| $\Mu$                    | \Mu                  | $\mu$                    | \mu                  |
| $\Nu$                    | \Nu                  | $\nu$                    | \nu                  |
| $\Xi$,$\varXi$           | \Xi,\varXi           | $\xi$                    | \xi                  |
| $\Omicron$               | \Omicron             | $\omicron$               | \omicron             |
| $\Pi$,$\varPi$           | \Pi,\varPi           | $\pi$,$\varpi$           | \pi,\varpi           |
| $\Rho$                   | \Rho                 | $\rho$,$\varrho$         | \rho,\varrho         |
| $\Sigma$,$\varSigma$     | \Sigma,\varSigma     | $\sigma$,$\varsigma$     | \sigma,\varsigma     |
| $\Tau$                   | \Tau                 | $\tau$                   | \tau                 |
| $\Upsilon$,$\varUpsilon$ | \Upsilon,\varUpsilon | $\upsilon$               | \upsilon             |
| $\Phi$,$\varPhi$         | \Phi,\varPhi         | $\phi$,$\varphi$         | \phi,\varphi         |
| $\Chi$                   | \Chi                 | $\chi$                   | \chi                 |
| $\Psi$,$\varPsi$         | \Psi,\varPsi         | $\psi$                   | \psi                 |
| $\Omega$,$\varOmega$     | \Omega,\varOmega     | $\omega$                 | \omega               |

<!-- more -->

### 1.2 二元关系符号
所有的二元关系符都可以加\not前缀得到相反意义的关系符。 比如`$\not\doteq$`$\to \not\doteq$

| 符号          | 格式        | 符号          | 格式        | 符号      | 格式     |
| ------------- | ----------- | ------------- | ----------- | --------- | -------- |
| $<$           | <           | $>$           | >           | $=$       | =        |
| $\le$         | \leq,\le    | $\ge$         | \geq,\ge    | $\equiv$  | \equiv   |
| $\ll$         | \ll         | $\gg$         | \gg         | $\doteq$  | \doteq   |
| $\prec$       | \prec       | $\succ$       | \succ       | $\sim$    | \sim     |
| $\preceq$     | \preceq     | $\succeq  $   | \succeq     | $\simeq$  | \simeq   |
| $\subset$     | \subset     | $\supset$     | \supset     | $\approx$ | \approx  |
| $\subseteq$   | \subseteq   | $\supseteq$   | \supseteq   | $\cong$   | \cong    |
| $\sqsubset$   | \sqsubset   | $\sqsupset$   | \sqsupset   | $\Join$   | \Join    |
| $\sqsubseteq$ | \sqsubseteq | $\sqsupseteq$ | \sqsupseteq | $\bowtie$ | \bowtie  |
| $\in$         | \in         | $\ni$         | \ni,\owns   | $\propto$ | \propto  |
| $\vdash$      | \vdash      | $\dashv$      | \dashv      | $\models$ | \models  |
| $\mid$        | \mid        | $\parallel$   | \parallel   | $\perp$   | \perp    |
| $\smile$      | \smile      | $\frown$      | \frown      | $\asymp$  | \asymp   |
| $:$           | :           | $\notin$      | \notin      | $\neq$    | \neq,\ne |


### 1.3 二元运算符
| 符号             | 格式           | 符号               | 格式             | 符号             | 格式           |
| ---------------- | -------------- | ------------------ | ---------------- | ---------------- | -------------- |
| $+$              | +              | $-$                | -                | $\mod{a}$        | \mod{a}        |
| $\pm$            | \pm            | $\mp$              | \mp              | $\triangleleft$  | \triangleleft  |
| $\cdot$          | \cdot          | $\div$             | \div             | $\triangleright$ | \triangleright |
| $\times$         | \times         | $\setminus$        | \setminus        | $\star$          | \star          |
| $\cup$           | \cup           | $\cap$             | \cap             | $\ast$           | \ast           |
| $\sqcup$         | \sqcup         | $\sqcap$           | \sqcap           | $\circ$          | \circ          |
| $\vee$           | \vee,\lor      | $\wedge$           | \wedge,\land     | $\bullet $       | \bullet        |
| $\oplus$         | \oplus         | $\ominus$          | \ominus          | $\diamond$       | \diamond       |
| $\odot$          | \odot          | $\oslash$          | \oslash          | $\uplus$         | \uplus         |
| $\otimes$        | \otimes        | $\bigcirc$         | \bigcirc         | $\amalg$         | \amalg         |
| $\bigtriangleup$ | \bigtriangleup | $\bigtriangledown$ | \bigtriangledown | $\dagger$        | \dagger        |
| $\lhd$           | \lhd           | $\rhd$             | \rhd             | $\ddagger$       | \ddagger       |
| $\unlhd$         | \unlhd         | $\unrhd$           | \unrhd           | $\wr$            | \wr            |

对于求模表达式，有\bmod和\pmod命令，前者相当于一个二元运算符，后者作为同余表达式的后缀：

| 符号        | 格式     | 符号       | 格式     |
| ----------- | -------- | ---------- | -------- |
| $\bmod {a}$ | \bmod{a} | $\pmod{a}$ | \pmod{a} |

### 1.4 巨算符
===  "巨算符"
    | 符号         | 格式       | 符号        | 格式      |
    | ------------ | ---------- | ----------- | --------- |
    | $\sum     $  | \sum       | $\prod   $  | \prod     |
    | $\bigcup  $  | \bigcup    | $\bigcap $  | \bigcap   |
    | $\bigvee  $  | \bigvee    | $\bigwedge$ | \bigwedge |
    | $\bigsqcup$  | \bigsqcup  | $\coprod $  | \coprod   |
    | $\bigoplus$  | \bigoplus  | $\bigodot$  | \bigodot  |
    | $\bigotimes$ | \bigotimes | $\biguplus$ | \biguplus |
    | $\int     $  | \int       | $\oint   $  | \oint     |
    | $\iint    $  | \iint      | $\oiint  $  | \oiint    |
    | $\iiint    $ | \iiint     | $\oiiint  $ | \oiiint   |

===  "示例"
    **累加**    $\sum_{k=1}^n\frac{1}{k}  \qquad  \displaystyle\sum_{k=1}^n\frac{1}{k}$

    **累乘**    $\prod_{k=1}^n\frac{1}{k}  \qquad  \displaystyle\prod_{k=1}^n\frac{1}{k}$

    **积分**    $\displaystyle \int_0^1xdx  \qquad  \iint_{D_{xy}}  \qquad  \iiint_{\Omega_{xyz}}$

### 1.5 文本/数学关系通用符号
| 符号 | 格式 | 符号 | 格式 |
| ---- | ---- | ---- | ---- |
| $\{$ | \\{  | $\}$ | \\}  |
| $\$$ | \\$  | $\%$ | %    |

### 1.6 箭头
| 符号                 | 格式               | 符号                  | 格式                |
| -------------------- | ------------------ | --------------------- | ------------------- |
| $\leftarrow       $  | \leftarrow,\gets   | $\rightarrow      $   | \rightarrow, \to    |
| $\longleftarrow   $  | \longleftarrow     | $\longrightarrow   $  | \longrightarrow     |
| $\leftrightarrow  $  | \leftrightarrow    | $\longleftrightarrow$ | \longleftrightarrow |
| $\Leftarrow       $  | \Leftarrow         | $\Rightarrow       $  | \Rightarrow         |
| $\Longleftarrow   $  | \Longleftarrow     | $\Longrightarrow   $  | \Longrightarrow     |
| $\Leftrightarrow  $  | \Leftrightarrow    | $\Longleftrightarrow$ | \Longleftrightarrow |
| $\mapsto          $  | \mapsto            | $\longmapsto       $  | \longmapsto         |
| $\hookleftarrow   $  | \hookleftarrow     | $\hookrightarrow   $  | \hookrightarrow     |
| $\leftharpoonup   $  | \leftharpoonup     | $\rightharpoonup   $  | \rightharpoonup     |
| $\leftharpoondown $  | \leftharpoondown   | $\rightharpoondown $  | \rightharpoondown   |
| $\leftrightharpoons$ | \leftrightharpoons | $\rightleftharpoons$  | \rightleftharpoons  |
| $\uparrow         $  | \uparrow           | $\downarrow        $  | \downarrow          |
| $\Uparrow         $  | \Uparrow           | $\Downarrow        $  | \Downarrow          |
| $\updownarrow     $  | \updownarrow       | $\Updownarrow      $  | \Updownarrow        |
| $\nearrow         $  | \nearrow           | $\searrow          $  | \searrow            |
| $\swarrow         $  | \swarrow           | $\nwarrow          $  | \nwarrow            |
| $\leadsto         $  | \leadsto           | $\iff              $  | \iff                |

另外，`\xleftarrow`和`\xrightarrow`命令提供了长度可以伸展的箭头，并且可以为箭头增加上下标：

| 符号                     | 格式                   | 符号                         | 格式                       |
| ------------------------ | ---------------------- | ---------------------------- | -------------------------- |
| $a \xleftarrow{x+y+z} b$ | a \xleftarrow{x+y+z} b | $c \xrightarrow[x<y]{abc} d$ | c \xrightarrow[x<y]{abc} d |

​

### 1.7 数学重音符号
| 符号              | 格式            | 符号        | 格式      | 符号            | 格式          |
| ----------------- | --------------- | ----------- | --------- | --------------- | ------------- |
| $\hat{a}     $    | \hat{a}         | $\vec{a} $  | \vec{a}   | $\mathring{a}$  | \mathring{a}  |
| $\bar{a} $        | \bar{a}         | $\acute{a}$ | \acute{a} | $\breve{a}    $ | \breve{a}     |
| $\check{a}$       | \check{a}       | $\grave{a}$ | \grave{a} | $\tilde{a}    $ | \tilde{a}     |
| $\dot{a} $        | \dot{a}         | $\ddot{a}$  | \ddot{a}  | $\widehat{AAA}$ | \widehat{AAA} |
| $\widetilde{AAA}$ | \widetilde{AAA} |

### 1.8 作为重音的箭头符号
| 符号                      | 格式                    | 符号                       | 格式                     |
| ------------------------- | ----------------------- | -------------------------- | ------------------------ |
| $\overleftarrow{AB}    $  | \overleftarrow{AB}      | $\overrightarrow{AB}    $  | \overrightarrow{AB}      |
| $\underleftarrow{AB}   $  | \underleftarrow{AB}     | $\underrightarrow{AB}   $  | \underrightarrow{AB}     |
| $\overleftrightarrow{AB}$ | \overleftrightarrow{AB} | $\underleftrightarrow{AB}$ | \underleftrightarrow{AB} |

### 1.9 上下直线与上下括号
上下直线格式如下，可叠加使用：

| 符号                       | 格式                     | 符号                         | 格式                       |
| -------------------------- | ------------------------ | ---------------------------- | -------------------------- |
| $\overline{AB}          $  | \overline{AB}            | $\underline{AB}           $  | \underline{AB}             |
| $\overline{\overline{AB}}$ | \overline{\overline{AB}} | $\underline{\underline{AB}}$ | \underline{\underline{AB}} |

`\overbrace`和`\underbrace`命令用来生成上/下括号，各自可带一个上/下标公式：

| 符号                    | 格式                  | 符号                     | 格式                   |
| ----------------------- | --------------------- | ------------------------ | ---------------------- |
| $\overbrace{a+b+c}^{6}$ | \overbrace{a+b+c}^{6} | $\underbrace{d+e+f}_{7}$ | \underbrace{d+e+f}_{7} |

### 1.10 定界符/括号修饰
| 符号      | 格式          | 符号         | 格式        |
| --------- | ------------- | ------------ | ----------- |
| $($       | (             | $)$          | )           |
| $[$       | [, \lbrack    | $]$          | ], \rbrack  |
| $\{$      | \\{,  \lbrace | $\}$         | \\} \rbrace |
| $\vert$   | \|, \vert     | $\Vert$      | \| ,\Vert   |
| $\lceil$  | \lceil        | $\rceil$     | \rceil      |
| $\lfloor$ | \lfloor       | $\rfloor$    | \rfloor     |
| $\langle$ | \langle       | $\rangle$    | \rangle     |
| $/    $   | /             | $\backslash$ | \backslash  |

使用`\left`和`\right`命令可令定界符的大小可变，在行间公式中常用。LATEX会自动根据括号内的公式大小决定定界符大小。`\left`和`\right`必须成对使用。需要使用单个定界符时，另一个定界符写成`\left.`或`\right.`。

| 符号                                                | 格式                                        |
| --------------------------------------------------- | ------------------------------------------- |
| $1+\left(\frac{1}{1-x^{2}}\right)^3 \qquad$         | `1+\left(\frac{1}{1-x^{2}}\right)^3 \qquad` |
| $\left.\frac{\partial f}{\partial t}\right\|_{t=0}$ | `\left.\frac{\partial f}{\partial t}\right  | _{t=0}` |


有时我们不满意于LATEX为我们自动调节的定界符大小。这时我们还可以用`\big`、`\bigg`等命令生成固定大小的定界符。更常用的形式是类似\left的`\bigl`、`\biggl`等，以及类似\right的`\bigr`、`\biggr`等（\bigl和\bigr不必成对出现）。

使用\big和\bigg等命令的另外一个好处是：用\left和\right分界符包裹的公式块是不允许断行的，所以也不允许在多行公式里跨行使用，而\big和\bigg等命令不受限制。

| 正常 | 格式 | 正常+1    | 格式    | 正常+2    | 格式    | 正常+3     | 格式     | 正常+4     | 格式     |
| ---- | ---- | --------- | ------- | --------- | ------- | ---------- | -------- | ---------- | -------- |
| $($  | (    | $\bigl($  | \bigl(  | $\Bigl($  | \Bigl(  | $\biggl($  | \biggl(  | $\Biggl($  | \Biggl(  |
| $\}$ | \}   | $\bigl\}$ | \bigl\} | $\Bigl\}$ | \Bigl\} | $\biggl\}$ | \biggl\} | $\Biggl\}$ | \Biggl\} |
| $\|$ | \|   | $\bigl\|$ | \bigl\| | $\Bigl\|$ | \Bigl\| | $\biggl\|$ | \biggl\| | $\Biggl\|$ | \Biggl\| |

**大定界符**

| 符号          | 格式        | 符号          | 格式        |
| ------------- | ----------- | ------------- | ----------- |
| $\lgroup   $  | \lgroup     | $\rgroup   $  | \rgroup     |
| $\lmoustache$ | \lmoustache | $\rmoustache$ | \rmoustache |

### 1.11 其他符号
| 符号           | 格式         | 符号         | 格式           | 符号        | 格式             |
| -------------- | ------------ | ------------ | -------------- | ----------- | ---------------- |
| $\dots      $  | \dots        | $\cdots  $   | \cdots         | $\vdots$    | \vdots           |
| $\ddots     $  | \ddots       | $\imath   $  | \imath         | $\jmath$    | \jmath           |
| $\hbar      $  | \hbar        | $\ell     $  | \ell           | $\wp  $     | \wp              |
| $\Re        $  | \Re          | $\Im      $  | \Im            | $\aleph$    | \aleph           |
| $\forall    $  | \forall      | $\exists  $  | \exists,\exist | $\mho$      | \mho             |
| $’          $  | ′            | $\prime   $  | \prime         | $\emptyset$ | \emptyset,\empty |
| $\partial   $  | \partial     | $\infty   $  | \infty         | $\nabla$    | \nabla           |
| $\triangle  $  | \triangle    | $\Box     $  | \Box           | $\Diamond$  | \Diamond         |
| $\diamondsuit$ | \diamondsuit | $\heartsuit$ | \heartsuit     | $\bot $     | \bot             |
| $\clubsuit  $  | \clubsuit    | $\spadesuit$ | \spadesuit     | $\top $     | \top             |
| $\flat      $  | \flat        | $\natural $  | \natural       | $\sharp$    | \sharp           |
| $\angle     $  | \angle       | $\neg     $  | \neg, \lnot    | $\surd$     | \surd            |
| $\therefore$   | \therefore   | $\because$   | \because       |

### 1.12 作为算符的函数
不带上下限的算符：

| 符号      | 格式    | 符号    | 格式  | 符号      | 格式    | 符号      | 格式    |
| --------- | ------- | ------- | ----- | --------- | ------- | --------- | ------- |
| $\sin$    | \sin    | $\cos$  | \cos  | $\tan$    | \tan    | $\cot$    | \cot    |
| $\sec$    | \sec    | $\csc$  | \csc  | $\arcsin$ | \arcsin | $\arccos$ | \arccos |
| $\arctan$ | \arctan | $\sinh$ | \sinh | $\cosh$   | \cosh   | $\tanh$   | \tanh   |
| $\coth $  | \coth   | $\arg$  | \arg  | $\exp  $  | \exp    | $\dim  $  | \dim    |
| $\log$    | \log    | $\lg$   | \lg   | $\ln$     | \ln     | $\ker$    | \ker    |
| $\hom  $  | \hom    | $\deg$  | \deg  |

带上下限的算符：

| 符号   | 格式  | 符号      | 格式     | 符号      | 格式     | 符号   | 格式 |
| ------ | ----- | --------- | -------- | --------- | -------- | ------ | ---- |
| $\lim$ | \lim⁡ | $\limsup$ | \limsup⁡ | $\liminf$ | \liminf⁡ | $\det$ | \det |
| $\sup$ | \sup⁡ | $\inf$    | \inf⁡    | $\min$    | \min⁡    | $\max$ | \max |
| $\Pr$  | \Pr⁡  | $\gcd$    | \gcd     |

### 1.13 自定义关系符和算符
可以通过命令`\stackrel{符号1}{符号2}`自定义二元关系符，该命令将前一个符号（符号1）叠加在后面的二元关系符（符号2）之上。
>$\stackrel{符号1}{符号2}$

---
## 2. 数学公式排版
数学公式有两种排版方式：

- 其一是与文字混排，称为**行内公式**；
- 其二是单独列为一行排版，称为**行间公式**。

行内公式由一对`$`在同一行包裹；行间公式由一对`$$`在上下行包裹。

行内公式和行间公式的行为在不同情况下可能有所差异。为了与文字相适应，行内公式在排版大的公式元素（分式、巨算符等）时显得很“局促”。

如对于`e=\lim_{n\rightarrow\infty}(1+\frac{1}{n})^{n}`来说，


<div class="grid cards" markdown>

-   :material-cat:{ .lg .middle .red} __行内公式__

    ---

    $e=\lim_{n\rightarrow\infty}(1+\frac{1}{n})^{n}$


-   :material-dog:{ .lg .middle .green} __行间公式__

    ---
    $$e=\lim_{n\rightarrow\infty}(1+\frac{1}{n})^{n}$$

</div>

当进入公式排版时，输入的空格和换行将被忽略。若要换行，可使用命令\\\\。

### 2.1 间距
数学符号的间距默认由符号的性质（关系符号、运算符等）决定。

若需要手动调整间距，有以下几种命令：

| 命令   | 样例         | 命令 | 样例    |
| ------ | ------------ | ---- | ------- |
| NO GAP | $aa$         | \\,  | $a \,a$ |
| \\     | $a \ a$      | \\:  | $a \:a$ |
| \quad  | $a \quad a$  | \\;  | $a \;a$ |
| \qquad | $a \qquad a$ | \\!  | $a \!a$ |

### 2.2 公式标号
使用`\tag{}`可以为公式手动标号：

`e^{i\pi}+1=0\tag{1.1}`
!!! note ""
    $$e^{i\pi}+1=0\tag{1.1}$$

<!-- $$
\begin{equation}
x^n+y^n=z^n 
\end{equation}
$$ -->

### 2.3 上标和下标
可用`^`和`_`标明上下标。注意上下标的内容一般需要用花括号包裹，否则上下标只对后面的一个符号起作用。

导数符号`'`是一类特殊的上标，可以适当连用表示多阶导数，也可以在其后连用上标。

| 符号      | 格式    |
| --------- | ------- |
| $2^ab$    | 2^ab    |
| $2^{ab}$  | 2^{ab}  |
| $f'''(x)$ | f'''(x) |

上标和下标可以通过\\\\换行。


### 2.4 根号
一般的根式使用`\sqrt{}`，表示2次方根；表示n次方根时写成`\sqrt[n]{}`。

| 符号          | 格式        |
| ------------- | ----------- |
| $\sqrt{2}$    | \sqrt{2}    |
| $\sqrt[3]{2}$ | \sqrt[3]{2} |

### 2.5 分式和巨算符
分式使用`\frac{分子}{分母}`来书写。分式的大小在行间公式中是正常大小，而在行内公式中被极度压缩。

命令`\dfrac`可令用户在行内使用正常大小的分式，如`\dfrac{1}{2}`显示为$\dfrac{1}{2}$

命令`\tfrac`可令用户在行间使用缩小后的分式，如`\tfrac{1}{2}`显示为$\tfrac{1}{2}$
​
巨算符在行内公式和行间公式的大小和形状有区别。

巨算符的上下标位置可由`\limits`和`\nolimits`调整。前者令巨算符的上下标位于上下方；后者令巨算符的上下标位于右上方和右下方。

在行内公式中，`\sum_{i=1}^{n}i`、`\sum\limits_{i=1}^{n}i`和`\sum\nolimits_{i=1}^{n}i`如下：

在行间公式中，`\sum_{i=1}^{n}i`、`\sum\limits_{i=1}^{n}i`和`\sum\nolimits_{i=1}^{n}i`如下：

<div class="grid cards" markdown>
-   :material-cat:{ .lg .middle .orange} __行内公式__

    ---
    $\sum_{i=1}^{n}i$  、 $\qquad\sum\limits_{i=1}^{n}i$  、 $\qquad \sum\nolimits_{i=1}^{n}i$


-   :material-dog:{ .lg .middle .aqua} __行间公式__

    ---
    $$
    \sum_{i=1}^{n}i \\
    \sum\limits_{i=1}^{n}i\\
    \quad\sum\nolimits_{i=1}^{n}i
    $$
</div>


### 2.6 公式

#### 2.6.1 长公式折行
通常来讲应当避免写出超过一行而需要折行的长公式。如果一定要折行的话，习惯上优先在等号之前折行，其次在加号、减号之前，再次在乘号、除号之前。其它位置应当避免折行。

amsmath宏包的multline环境提供了书写折行长公式的方便环境。它允许用\\\\折行，将公式编号放在最后一行。多行公式的首行左对齐，末行右对齐，其余行居中。通常用`$$`包围公式会居中，用`$`包围公式会左对齐。

<div class="grid cards" markdown>

-   :material-cat:{ .lg .middle .yellow} __长公式折行代码__

    ---
    ```py
    $\begin{aligned}
    a + b + c + d + e + 
    f + g + h + i \\
    &= j + k + l + m + n\\
    &= o + p + q + r + s\\
    &= t + u + v + x + z
    \end{aligned}$
    ```

-   :material-dog:{ .lg .middle .blue} __长公式折行展示效果__

    ---
    $\begin{aligned}
    a + b + c + d + e + 
    f + g + h + i \\
    &= j + k + l + m + n\\
    &= o + p + q + r + s\\
    &= t + u + v + x + z
    \end{aligned}$
</div>

公式的最后一行不写\\\\，如果写了，反倒会产生一个多余的空行。

<div class="grid cards" markdown>

-   :material-cat:{ .lg .middle .green} __最后一行不要加\\\\__

    ---
    ```py
    $$
    \begin{cases}
    x=\rho\cos\theta \\
    y=\rho\sin\theta \\
    \end{cases}
    $$
    ```

-   :material-dog:{ .lg .middle .purple} __不加\\\\展示效果__

    ---
    $$
    \begin{cases}
    x=\rho\cos\theta \\
    y=\rho\sin\theta \\
    \end{cases}
    $$
</div>

还有, 不要在公式内使用中文, 除非是 `$\text{中文}$`$\text{中文}$(但是也不推荐)

#### 2.6.2 多行公式
更多的情况是，我们需要罗列一系列公式，并令其按照等号对齐。目前最常用的是align环境，它将公式用&隔为两部分并对齐。分隔符通常放在等号左边：

<div class="grid cards" markdown>

-   :material-cat:{ .lg .middle .aqua} __aligned MD代码__

    ---
    ```py
    $$
    \begin{aligned}
    a & = b + c \\
    & = d + e
    \end{aligned}
    $$
    ```

-   :material-dog:{ .lg .middle .red} __aligned 展示效果__

    ---
    $$
    \begin{aligned}
    a & = b + c \\
    & = d + e
    \end{aligned}
    $$
</div>

aligned还能够对齐多组公式，除等号前的&之外，公式之间也用&分隔：

<div class="grid cards" markdown>

-   :material-cat:{ .lg .middle .blue} __对齐多组公式 MD代码__

    ---
    ```py
    $$
    \begin{aligned}
    a &=1  &  b &=2   & c &=3   \\
    d &=-1 &  e &=-2  & f &=-5
    \end{aligned}
    $$
    ```

-   :material-dog:{ .lg .middle .orange} __对齐多组公式 展示效果__

    ---
    $$
    \begin{aligned}
    a &=1  &  b &=2   & c &=3   \\
    d &=-1 &  e &=-2  & f &=-5
    \end{aligned}
    $$
</div>

如果我们不需要按等号对齐，只需罗列数个公式，gather将是一个很好用的环境：

<div class="grid cards" markdown>

-   :material-cat:{ .lg .middle .purple} __gather MD代码__

    ---
    ```PY
    $$
    \begin{gather}
    a = b + c \\
    d = e + f + g \\
    h + i = j + k \\
    l + m = n
    \end{gather}
    $$
    ```

-   :material-dog:{ .lg .middle .yellow} __gather 展示效果__

    ---
    $$
    \begin{gather}
    a = b + c \\
    d = e + f + g \\
    h + i = j + k \\
    l + m = n
    \end{gather}
    $$
</div>

#### 2.6.3 分支公式
使用cases环境可支持分支公式：

<div class="grid cards" markdown>

-   :material-cat:{ .lg .middle .red} __cases MD代码__

    ---
    ```py
    $$
    |x| =
    \begin{cases}
    -x & \text{if } x < 0,\\
    0 & \text{if } x = 0,\\
    x & \text{if } x > 0.
    \end{cases}
    $$
    ```

-   :material-dog:{ .lg .middle .green} __cases 展示效果__

    ---
    $$
    |x| =
    \begin{cases}
    -x & \text{if } x < 0,\\
    0 & \text{if } x = 0,\\
    x & \text{if } x > 0.
    \end{cases}
    $$
</div>

### 2.7 矩阵
amsmath宏包直接提供了多种排版矩阵的环境，包括不带定界符的`matrix`，以及带各种定界符的矩阵`pmatrix`（( ）、`bmatrix`（[ ）、`Bmatrix`（\{）、`vmatrix`（|）、`Vmatrix`（∥）。

- 不带定界符的`matrix`
<div class="grid cards" markdown>

-   :material-cat:{ .lg .middle .orange} __matrix MD代码__

    ---
    ```py
    $$
    \begin{matrix}
    1 & 2 \\ 3 & 4
    \end{matrix}
    $$
    ```

-   :material-dog:{ .lg .middle .aqua} __matrix 展示效果__

    ---
    $$
    \begin{matrix}
    1 & 2 \\ 3 & 4
    \end{matrix} \qquad
    $$

</div>


- 带定界符的矩阵`pmatrix`（( ）
<div class="grid cards" markdown>

-   :material-cat:{ .lg .middle .yellow} __pmatrix MD代码__

    ---
    ```py
    $$
    \begin{pmatrix}
    x_{11} & x_{12} & \ldots & x_{1n}\\
    x_{21} & x_{22} & \ldots & x_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    x_{n1} & x_{n2} & \ldots & x_{nn}\\
    \end{pmatrix} 
    $$
    ```

-   :material-dog:{ .lg .middle .blue} __pmatrix 展示效果__

    ---
    $$
    \begin{pmatrix}
    x_{11} & x_{12} & \ldots & x_{1n}\\
    x_{21} & x_{22} & \ldots & x_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    x_{n1} & x_{n2} & \ldots & x_{nn}\\
    \end{pmatrix} 
    $$

</div>

- 带定界符的矩阵`bmatrix`（[ ）、`Bmatrix`（\{）
=== "bmatrix MD代码 "
    !!! note ""
        ```py
        $$
        \begin{bmatrix}
        1 & 2 \\ 3 & 4
        \end{bmatrix} 
        $$
        ```

=== "bmatrix 展示效果 "
    !!! note ""
        $$
        \begin{bmatrix}
        1 & 2 \\ 3 & 4
        \end{bmatrix} 
        $$

=== "Bmatrix MD代码 "
    !!! note ""
        ```py
        $$
        \begin{Bmatrix}
        1 & 2 \\ 3 & 4
        \end{Bmatrix}
        $$
        ```
=== "Bmatrix 展示效果 "
    !!! note ""
        $$
        \begin{Bmatrix}
        1 & 2 \\ 3 & 4
        \end{Bmatrix}
        $$

- 带定界符的矩阵`vmatrix`（|）、`Vmatrix`（∥）
=== "vmatrix MD代码 "
    !!! note ""
        ```py
        $$
        \begin{vmatrix}
        1 & 2 \\ 3 & 4
        \end{vmatrix}
        $$
        ```
=== "vmatrix 展示效果 "
    !!! note ""
        $$
        \begin{vmatrix}
        1 & 2 \\ 3 & 4
        \end{vmatrix}
        $$

=== "Vmatrix MD代码 "
    !!! note ""
        ```PY
        $$
        \begin{Vmatrix}
        1 & 2 \\ 3 & 4
        \end{Vmatrix}
        $$
        ```

=== "Vmatrix 展示效果 "
    !!! note ""
        $$
        \begin{Vmatrix}
        1 & 2 \\ 3 & 4
        \end{Vmatrix}
        $$

### 2.8 数学字母字体
LATEX允许一部分数学符号切换字体，主要是拉丁字母、数字、大写希腊字母以及重音符号等。

| 示例                        | 命令                      | 注             |
| --------------------------- | ------------------------- | -------------- |
| $\mathrm{ABCDEabcde1234} $  | \mathrm{ABCDEabcde1234}   |                |
| $\mathit{ABCDEabcde1234} $  | \mathit{ABCDEabcde1234}   |                |
| $\mathbf{ABCDEabcde1234} $  | \mathbf{ABCDEabcde1234}   |                |
| $\mathsf{ABCDEabcde1234} $  | \mathsf{ABCDEabcde1234}   |                |
| $\mathtt{ABCDEabcde1234} $  | \mathtt{ABCDEabcde1234}   |                |
| $\mathcal{ABCDE1234}  $     | \mathcal{ABCDE1234}       | 不提供小写字母 |
| $\mathscr{ABCDE} $          | \mathscr{ABCDE}           | 仅提供大写字母 |
| $\mathfrak{ABCDEabcde1234}$ | \mathfrak{ABCDEabcde1234} |                |
| $\mathbb{ABCDE}$            | \mathbb{ABCDE}            | 仅提供大写字母 |

### 2.9 数学符号的尺寸
数学符号按照符号排版的位置规定尺寸，从大到小包括行间公式尺寸、行内公式尺寸、上下标尺寸、次级上下标尺寸。除了字号有别之外，行间和行内公式尺寸下的巨算符也使用不一样的大小。LATEX为每个数学尺寸指定了一个切换的命令：

| 命令                       | 尺寸           | 示例                         |
| -------------------------- | -------------- | ---------------------------- |
| \displaystyle{\sum a}      | 行间公式尺寸   | $\displaystyle{\sum a}   $   |
| \textstyle{\sum a}         | 行内公式尺寸   | $\textstyle{\sum a}      $   |
| \scriptstyle{\sum a}       | 上下标尺寸     | $\scriptstyle{\sum a}   $    |
| \scriptscriptstyle{\sum a} | 次级上下标尺寸 | $\scriptscriptstyle{\sum a}$ |

### 2.10 加粗的数学符号
可使用`\mathbf`（\bold）命令加粗字体，但`\mathbf`（\bold）只能改变拉丁字母和大写希腊字母，小写希腊字母就没有用。

amsmath提供了一个\boldsymbol命令，可将本身支持粗体符号的数学字体切换为粗体版本。

| 符号                                   | 格式                                   |
| -------------------------------------- | -------------------------------------- |
| $\mathbf{A\ a\ \Omega\ \omega\ 1}$     | `\mathbf{A\ a\ \Omega\ \omega\ 1}`     |
| $\boldsymbol{A\ a\ \Omega\ \omega\ 1}$ | `\boldsymbol{A\ a\ \Omega\ \omega\ 1}` |



