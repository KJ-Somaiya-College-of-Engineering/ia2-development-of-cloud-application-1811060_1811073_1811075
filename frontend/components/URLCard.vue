<template>
  <div class="column is-one-quarter">
    <div class="card">
      <div class="card-header">
        <div class="card-header-title">
          <small><i><font color="#3c7962">https://trcr.tk/{{urlObj._id}}</font></i></small>
        </div>
        <div class="card-header-icon">
          <button class="button is-small is-primary is-light" v-on:click.prevent="copy(urlObj._id)">Copy</button>
        </div>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <div class="columns">
              <div class="column is-8">
                <p class="title is-5 shortned" v-if="urlObj.title">
                  {{ applyShortening(urlObj.title) }}
                </p>
                <p class="title is-5 shortned" v-else>
                  {{ applyShortening(getDomain(urlObj.redirect_url)) }}
                </p>
              </div>
              <div class="column is-2 is-offset-1">
                <button class="button is-danger is-light" v-on:click.prevent="delete_url(urlObj._id)" v-if="!isDeleting">
                  <span class="icon is-small">
                        <i class="fa fa-trash-alt"></i>
                    </span>
                </button>
                <button class="button is-danger is-light is-loading" v-else />
              </div>
            </div>
          </div>
        </div>

        <div class="content">
          <div style="padding-bottom: 4%;">
            <button class="button is-fullwidth is-light is-primary" v-on:click.prevent="isCustomiseCardActive = true">
              Customise
            </button>
          </div>
          <nuxt-link :to="'/monitor/'+urlObj._id">
            <div class="button is-fullwidth is-primary">
              <span class="icon is-small">
                <i class="fas fa-chart-bar"></i> </span
              >&nbsp;&nbsp;&nbsp; Analyse
            </div>
          </nuxt-link>
        </div>
      </div>
    </div>
    <b-modal v-model="isCustomiseCardActive" :width="740" scroll="keep">
      <customise-card :urlObj="urlObj" :closeCustomiseCard="closeCustomiseCard"/>    
    </b-modal>
  </div>
</template>

<script>
import timeDiffernce from "@/functions/timeDifference";
import deleteUrl from "@/functions/deleteUrl";
import CustomiseCard from "./CustomiseCard.vue";
export default {
  components: { CustomiseCard },
  props: {
    urlObj: {
      type: Object,
      required: true,
    },
  },
  data(){
    return{
      isCustomiseCardActive: false,
      isDeleting: false
    }
  },
  methods: {
    copy(id) {
      this.$clipboard(`https://trcr.tk/${id}`);
      this.$toasted.success("URL Copied Successfully.", {
          theme: "outline",
          position: "top-right",
          duration: 3000
      })
    },
    getDomain(url) {
      const arr = url.split("/");
      const result = arr[2];

      return url;
    },
    applyShortening(string) {
      if (string.length > 10) {
        const str1 = string.substr(0, 24);
        const str2 = "...";
        return str1 + str2;
      }
      return string;
    },
    closeCustomiseCard(status, message){
      this.isCustomiseCardActive = false
      if(status){
        this.$toasted.success(message, {
          theme: "outline",
          position: "top-right",
          duration: 3000
        })
      } 
      else {
        this.$toasted.error(message, {
          theme: "outline",
          position: "top-right",
          duration: 3000
        })
      }
        
    },
    parsed(created_ts) {
      if (created_ts == "Just Now") {
        return "Just Now";
      }
      var currentDate = new Date(created_ts * 1000);
      const tdiff = timeDiffernce(new Date(), currentDate);
      if (tdiff) return tdiff;
      const monthNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];

      var date = currentDate.getDate();
      var month = currentDate.getMonth();
      var year = currentDate.getFullYear();

      return date + " " + monthNames[month + 1] + " " + year;
    },
    async delete_url(urlid){
      this.isDeleting = true;
      const status = await deleteUrl(urlid, this);
      if(status) {
        this.$store.dispatch('deleteUrlEntry', urlid);
        this.$toasted.success(`Deleted ${this.urlObj.title} Successfully!`, {
          theme: "outline",
          position: "top-right",
          duration: 3500
        })
      } else {
        this.$toasted.error("Error Deleting URL", {
          theme: "outline",
          position: "top-right",
          duration: 3500
        })
      }
      this.isDeleting = false;
    },
  },
};
</script>

<style>
</style>