<template>
  <div>
    <h1>Follow 정보</h1>
    
    <div>
      <h3>Followers:</h3>
      <ul>
        <li v-for="follower in followers" :key="follower.id">
          {{ follower.nickname }}
        </li>
      </ul>
    </div>

    <div>
      <h3>Following:</h3>
      <ul>
        <li v-for="following in followings" :key="following.id">
          {{ following.nickname }}
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
export default {
  name: 'FollowView',
  props: ['followers', 'followings'],
  created() {
    const followers = this.$route.query.followers;
    const followings = this.$route.query.followings;

    // followers와 followings 데이터를 사용하여 원하는 작업 수행
    console.log(followers);
    console.log(followings);
  }
}
</script>

<style>

</style>