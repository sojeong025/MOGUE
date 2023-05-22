<template>
  <div>
    <h1>SearchView</h1>
    <button @click="Back"> 뒤로가기 </button>
    <div id="search">
      <input type="text" placeholder="작품명, 게시글, 배우를 검색해보세요.">
    </div>
    <div id="collection">
      <p>이런 컬렉션은 어때요? </p>
      <CollectionList/>
    </div>
  </div>
</template>

<script>
import CollectionList from '@/components/CollectionList'

export default {
  name: 'SearchView',
  components: {
    CollectionList,
  },
  methods: {
    Back(){
      this.$router.go(-1)
    }
  }
}
</script>

<style>
#search {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
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
#collection {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 50px;
  }
</style>