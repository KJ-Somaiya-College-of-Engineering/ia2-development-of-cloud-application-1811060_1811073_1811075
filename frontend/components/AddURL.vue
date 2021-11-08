<template>
    <form>
        <div class="field">
            <div class="control">
            <input class="input is-large" type="text" placeholder="Paste Your Link Here" v-model="redirectURL" />
            </div>
        </div>
            <div class="control">
                <button class="button is-large is-fullwidth is-primary is-loading" v-on:click.prevent="shorten()" v-if="isLoading">
                    <span class="icon is-small">
                        <i class="fas fa-compress-arrows-alt"></i>
                    </span>&nbsp;&nbsp;&nbsp;
                    Shorten
                </button>
                <button class="button is-large is-fullwidth is-primary" v-on:click.prevent="shorten()" v-else>
                    <span class="icon is-small">
                        <i class="fas fa-compress-arrows-alt"></i>
                    </span>&nbsp;&nbsp;&nbsp;
                    Shorten
                </button>
            </div>
            <b-modal v-model="isSuccessCardActive">
                <after-shorten-message :urlObj="finalUrlObject"/>
            </b-modal>
    </form>
</template>

<script>
import shortenURL from '@/functions/shortenURL'
import AfterShortenMessage from './AfterShortenMessage.vue';
export default {
  components: { AfterShortenMessage },
    data() {
        return {
            redirectURL: "",
            showSuccessNotification: false,
            showFailureNotification: false,
            isLoading: false,
            isSuccessCardActive: false,
            finalUrlObject: {},
        }
    },
    methods: {
        async shorten() {
            this.isLoading = true;
            if(!this.redirectURL) {
                this.isLoading = false;
                this.$toasted.error("No URL entered", {
                    theme: "outline",
                    position: "top-right",
                    duration: 3000
                })
                return
            };
            const val = await shortenURL(this.redirectURL, this);
            if(!val){
                this.$toasted.error("Invalid URL or Server Error ", {
                    theme: "outline",
                    position: "top-right",
                    duration: 3000
                })
                this.isLoading = false;
                this.redirectURL = "";
                return;
            }
            const { ID, OG_DETAILS } = val;
            if(ID){
                this.finalUrlObject = {
                    _id: ID,
                    hits: 0,
                    redirect_url: this.redirectURL,
                    created_ts: "Just Now",
                    title: OG_DETAILS?.title,
                    url_og: OG_DETAILS
                }
                this.$store.dispatch('addNewShortedUrlObject', this.finalUrlObject);
                this.isSuccessCardActive = true;
            } else {
                this.$toasted.error("Invalid URL or Server Error ", {
                    theme: "outline",
                    position: "top-right",
                    duration: 3000
                })
            }
            this.redirectURL = "";
            this.isLoading = false;
        }
    }
}
</script>

<style>

</style>