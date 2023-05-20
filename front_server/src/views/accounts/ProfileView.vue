<template>
  <div>
    <h1>Profile</h1>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  created() {
    console.log(localStorage['user_id'])
  }
}
</script>

<style>

</style>