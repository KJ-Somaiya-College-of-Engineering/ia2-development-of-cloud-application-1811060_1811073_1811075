<template>
  <section class="section">
    <div v-if="isLoading">
      <loading-screen/>
    </div>
    <div v-if="showErrorMessage">
      Error
    </div>
    <div class="columns is-multiline" v-else>
      <URLCard v-for="urlOb in allUrls" v-bind:key="urlOb._id" :urlObj="urlOb" />
    </div>
  </section>
</template>

<script>
import URLCard from "@/components/URLCard";

import fetchAllUrls from "@/functions/fetchAllUrls"
import LoadingScreen from './LoadingScreen.vue';

export default {
  components: { URLCard, LoadingScreen },
  data() {
    return {
      isLoading: false,
      showErrorMessage: false
    }
  },
  async mounted() {
    this.isLoading = true;
    const data = await fetchAllUrls(this);
    if(data){
      this.$store.dispatch('updateUrls', data);
    } else {
      this.showErrorMessage = true;
    }
    this.isLoading = false;
  },
  computed: {
    allUrls() {
      const sortedActivities = Array(...this.$store.state.urls)
      return sortedActivities.sort((a, b) =>b.created_ts - a.created_ts);
    }
  }
};
</script>

<style>
</style>