# :material-account-cowboy-hat-outline:{.orange} THEY PLAY GAMES :material-nintendo-game-boy:{.red}
!!! success ""

    **Wish everyone success, chose a color you like**

    <div class="mdx-switch">
    <!-- <button data-md-color-scheme="default"><code>:material-lightbulb-on:&nbsp;default&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-scheme="slate"><code>:material-lightbulb:&nbsp;slate&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <BR> -->
    <button data-md-color-primary="red"><code>red&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="pink"><code>pink&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="purple"><code>purple&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="deep-purple"><code>deep purple</code></button>
    <button data-md-color-primary="indigo"><code>indigo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="blue"><code>blue&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="light-blue"><code>light blue&nbsp;</code></button>
    <br>
    <button data-md-color-primary="cyan"><code>cyan&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="teal"><code>teal&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="green"><code>green&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="light-green"><code>light green</code></button>
    <button data-md-color-primary="lime"><code>lime&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="yellow"><code>yellow&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="amber"><code>amber&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <br>
    <button data-md-color-primary="orange"><code>orange&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="deep-orange"><code>deep orange</code></button>
    <button data-md-color-primary="brown"><code>brown&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="grey"><code>grey&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="blue-grey"><code>blue grey&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="black"><code>black&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    <button data-md-color-primary="white"><code>white&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code></button>
    </div>



<!-- 
<script>
  var buttons = document.querySelectorAll("button[data-md-color-scheme]")
  buttons.forEach(function(button) {
    button.addEventListener("click", function() {
      document.body.setAttribute("data-md-color-switching", "")
      var attr = this.getAttribute("data-md-color-scheme")
      document.body.setAttribute("data-md-color-scheme", attr)
      var name = document.querySelector("#__code_0 code span.l")
      name.textContent = attr
      setTimeout(function() {
        document.body.removeAttribute("data-md-color-switching")
      })
    })
  })
</script>
-->

<script>
  var buttons = document.querySelectorAll("button[data-md-color-primary]")
  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      var attr = this.getAttribute("data-md-color-primary")
      document.body.setAttribute("data-md-color-primary", attr)
      var name = document.querySelector("#__code_1 code span.l")
      name.textContent = attr.replace("-", " ")
    })
  })
</script>