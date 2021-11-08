<template>
  <div id="app">
    <OSChart :data="chartData"></OSChart>
  </div>
</template>

<script>
import OSChart from "~/charts/Pie";
export default {
    components: { OSChart },
    props: ["stats"],
    data() {
        return {
            chartData: {
                hoverBackgroundColor: "red",
                hoverBorderWidth: 10,
                labels: ["Mac OS X", "Linux", "Windows", "Android", "iOS", "Others"],
                datasets: [
                    {
                        label: "Operating Systems",
                        backgroundColor: ["#66d2b3", "#367362", "#1f4339", "#4aee53", "#04fe11", "36f362"],
                        data: this.stats,
                    },
                ],
            },
        };
    },
};
</script>

<style>
</style>