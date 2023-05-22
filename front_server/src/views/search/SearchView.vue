<template>
  <div>
    <h1>SearchView</h1>
    <button @click="Back"> 뒤로가기 </button>
    <div class="search">
      <input type="text" placeholder="작품명, 게시글, 배우를 검색해보세요.">
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchView',
  methods: {
    Back(){
      this.$router.go(-1)
    }
  }
}
</script>

<style>
.search {
  position: relative;
  width: 300px;
}
input {
  margin: 10px;
  width: 100%;
  border: 1px solid #bbb;
  border-radius: 8px;
  padding: 10px 12px;
  font-size: 14px;
}
</style>