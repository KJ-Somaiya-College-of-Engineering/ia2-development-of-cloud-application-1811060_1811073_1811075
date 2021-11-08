<template>
    <div class="columns">
        <div class="column id-one-fifth"></div>
        <div class="column">
            <div class="card">
                <div class="card-content" v-if="osStats">
                    <OS :stats="osStats" />
                </div>
            </div>
        </div>
        <div class="column">
            <div class="card">
                <div class="card-content" v-if="brandStats">
                    <Brands :stats="brandStats"/>
                </div>
            </div>
        </div>
        <div class="column">
            <div class="card">
                <div class="card-content" v-if="ramStats">
                    <RAMs :stats="ramStats"/>
                </div>
            </div>
        </div>
        <div class="column id-one-fifth"></div>
    </div>
</template>

<script>
import OS from '@/components/PieCharts/OS'
import Brands from '@/components/PieCharts/Brands'
import RAMs from '@/components/PieCharts/RAMs'

export default {
    components: { OS, Brands, RAMs },
    computed: {
        osStats() {
            const urlObj = this.$store.state.activeUrlObject;
            if(urlObj)
            return [urlObj.clicks.OS.MacOSX, urlObj.clicks.OS.Linux, urlObj.clicks.OS.Windows, urlObj.clicks.OS.Android, urlObj.clicks.OS.iOS, urlObj.clicks.OS.Other]
        },
        brandStats() {
            const urlObj = this.$store.state.activeUrlObject;
            if(urlObj)
            return [urlObj.clicks.Brands.Vivo, urlObj.clicks.Brands.Xiaomi, urlObj.clicks.Brands.Asus, urlObj.clicks.Brands.Nokia, urlObj.clicks.Brands.Apple, urlObj.clicks.Brands.Motorola, urlObj.clicks.Brands.Samsung, urlObj.clicks.Brands.Other]
        },
        ramStats() {
            const urlObj = this.$store.state.activeUrlObject;
            if(urlObj)
            return [urlObj.clicks.RAMs.TwoGB, urlObj.clicks.RAMs.FourGB, urlObj.clicks.RAMs.SixGB, urlObj.clicks.RAMs.EightGB, urlObj.clicks.RAMs.Other]
        }
    }
}
</script>

<style>

</style>