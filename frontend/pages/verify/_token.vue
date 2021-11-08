<template>
  <div>
      <h1 v-if="loginStatus == 0"><loading-screen/></h1>
      <h1 v-if="loginStatus == -1">Problem</h1>
  </div>
</template>

<script>
import LoadingScreen from '@/components/LoadingScreen'

import verifyTokenAndGetUser from '@/functions/verifyTokenAndGetUser'

export default {
    data() {
        return {
            token: this.$route.params.token,
            loginStatus: 0
        }
    },
    components: { LoadingScreen },
    async mounted() {
        const user = await verifyTokenAndGetUser(this.token, this)
        console.log(user)
        if(user) {
            this.$store.dispatch('updateUserAndToken', {user, token: this.token})
            this.loginStatus = 1;
            this.$router.push('/dashboard');
        } else {
            this.loginStatus = -1;
        }
    }
}
</script>

<style>

</style>