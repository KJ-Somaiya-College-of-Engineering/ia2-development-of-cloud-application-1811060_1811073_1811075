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
                labels: ["2 GB", "4 GB", "6 GB", "8 GB", "Others"],
                datasets: [
                    {
                        label: "RAMs",
                        backgroundColor: ["#66d2b3", "#367362", "#1f4339", "#4aee53", "04fe11"],
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