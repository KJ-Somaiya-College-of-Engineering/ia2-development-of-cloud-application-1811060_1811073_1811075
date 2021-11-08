<template>
    <div class="columns is-multiline" style="padding: 10%; padding-top: 0%; padding-bottom: 10%" v-if="collectedDataPoints">
        <DataPointCard v-for="dataPoint in collectedDataPoints" v-bind:key="dataPoint.dataid" :dataObject="dataPoint"/>
        <div v-if="!moreDataLoading">
            <button class="button is-light is-fullwidth" v-if="hasMorePages" v-on:click.prevent="fetchNext()">
                Load More Data
            </button>
        </div>
        <div class="loader" v-else>
            
        </div>
    </div>
    <div v-else>
        Some Error
    </div>
</template>

<script>
import DataPointCard from '@/components/DataPointCard'

export default {
    components: { DataPointCard },
    computed: {
        collectedDataPoints() {
            const _ = this.$store.state.update;
            return this.$store.state.collectedData[this.$route.params.urlid];
        },
        hasMorePages() {
            const _ = this.$store.state.update;
            return this.$store.getters.hasMorePages(this.$route.params.urlid)
        },
        moreDataLoading() {
            return this.$store.state.isMonitorLoading;
        }
    },
    methods: {
        fetchNext() {
            if(this.$store.getters.hasMorePages(this.$route.params.urlid)) {
                this.$store.dispatch('fetchNextPage', {urlid: this.$route.params.urlid, first: false})
            }
        }
    },
    mounted() {
        this.$store.dispatch('fetchNextPage', {urlid: this.$route.params.urlid, first: true});
    }
}
</script>