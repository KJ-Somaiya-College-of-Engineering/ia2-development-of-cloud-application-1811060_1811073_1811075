<template>
  <div>
        <URLDetails/>
        <hr/>
        <URLAnalytics/>
        <hr/>
        <CollectedData/>
  </div>
</template>

<script>
import CollectedData from '~/components/CollectedData.vue'
import URLDetails from '~/components/URLDetails.vue'
import URLAnalytics from '~/components/URLAnalytics'
export default {
  components: { URLDetails, CollectedData, URLAnalytics }
}
</script>

<style>

</style>