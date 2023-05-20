<template>
  <div>
    <h1>Singup Page</h1>
    <form id="signup-form" @submit.prevent="signUp">
      <label for="nickname"> 아이디 : </label>
      <input type="text" id="nickname" v-model="nickname" value="nickname">
      <button>중복 확인</button><br>

      <label for="email">이메일 : </label>
      <input type="email" id="email">

      <label for="password"> 비밀번호 : </label>
      <input type="password" id="password" v-model="password"><br>

      <label for="password2"> 비밀번호 확인 : </label>
      <input type="password" id="password2" v-model="password2"><br>

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView'
}
</script>

<style>

</style>