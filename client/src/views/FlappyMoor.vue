<template>
    <div id="sas">
    </div>
</template>

<script>
    export default{
        name: "FlappyMoor",
        mounted(){
            let phaserScript = document.createElement('script');
            phaserScript.setAttribute('src', '//cdn.jsdelivr.net/npm/phaser@3.21.0/dist/phaser.js');
            document.head.appendChild(phaserScript);
            let gameScript = document.createElement('script');
            gameScript.setAttribute('src', '../../flappyMoor/js/script.js');
            document.head.appendChild(gameScript);
        },
    }
</script>

<style scoped>

</style>
