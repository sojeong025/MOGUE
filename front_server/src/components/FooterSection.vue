<template>
  <div class="footer">
    <div class="footer-text">
      <p class="logo" >MOGUE</p>
      <br>
      <p>designed by &nbsp; | &nbsp; @d.ang.2&nbsp; @s_o_ing</p>
      <p class="down">@Copyright MOGUE. 모든 권리 보유.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FooterSection',
  
}
</script>

<style scoped>
.footer {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 300px;
  background-color: black;
  color: white;
}

.footer-text {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 12px;
}

.logo {
  font-size: 80px;
  font-weight: 100;
  border-bottom: 1px solid white;
  margin-bottom: 10px;
}

.down {
  color: rgb(165, 165, 165);
  margin-top: 6px;
}
</style>