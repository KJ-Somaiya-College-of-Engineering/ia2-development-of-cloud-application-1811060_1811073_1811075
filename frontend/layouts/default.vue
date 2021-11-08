<template>
  <div>
      <b-navbar>
        <template #brand>
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <div class="logob">や</div>
                <div class="titleb">TRACER</div>
            </b-navbar-item>
        </template>

        <template #end>
            <b-navbar-item tag="div" style="padding: 5%" v-if="!isLoggedIn">
                    <nuxt-link :to="'/register'" class="button is-primary">
                        <strong>Sign up</strong>
                    </nuxt-link> &nbsp; &nbsp;
                    <nuxt-link :to="'/login'" class="button is-light">
                        Log in
                    </nuxt-link>
            </b-navbar-item>
            <b-navbar-item tag="div" class="has-dropdown is-hoverable" style="padding: 5%" v-else>
                    <a class="navbar-link">
                        Hi, {{name}}!
                    </a>
                    <div class="navbar-dropdown">
                        <nuxt-link :to="'/dashboard'" class="navbar-item">
                            Dashboard
                        </nuxt-link>
                        <a v-on:click.prevent="logout()" class="navbar-item">
                            Logout
                        </a>
                    </div>
            </b-navbar-item>
        </template>
    </b-navbar>
    <nuxt/>
  </div>
</template>

<script>
export default {
    computed: {
        isLoggedIn(){
            return this.$store.state.isLoggedIn
        },
        name() {
            return this.$store.state.user?.NAME
        }
    },
    mounted() {
        this.$store.dispatch('fetchAndSetUser')
    },
    methods: {
        logout() {
            this.$store.dispatch('cleanupAndLogout');
            this.$router.push('/')
        }
    }
}
</script>

<style>
.logob {
  font-family: "Noto Serif JP", serif;
  font-size: 200%;
  color: #66d3b3;
  padding-right: 5%;
}

.titleb {
  font-size: 170%;
  font-family: 'Anton', sans-serif;
}
</style>