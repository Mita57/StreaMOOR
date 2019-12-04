<template>
    <v-container class="justify-center ma-0 pa-0">
        <!--channel tabs-->
        <v-tabs v-model="tab" height="50px" class="" dark icons-and-text>
            <v-tabs-slider></v-tabs-slider>
            <v-tab href="" class="flex-row">
                <img src="../assets/Igor.png" class="mr-2 ml-n2 mt-1" height="40px">
                Vitas
            </v-tab>

            <v-tab href="">
                Эфир
            </v-tab>

            <v-tab href="">
                Записи
            </v-tab>
            <v-divider></v-divider>
                <v-btn class="success mt-2" tile>Подписаться</v-btn>
            <v-tab disabled>Подписчиков: 1337228</v-tab>
        </v-tabs>
        <!--chat-->
        <v-navigation-drawer app clipped right>
            <v-list two-line subheader>
                <v-subheader inset>Чат:</v-subheader>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>10 Hours of vitas</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-responsive :aspect-ratio="16/9" class=" ma-8 mt-2">
            <v-img src="../assets/pic1.jpg"></v-img>
        </v-responsive>
        <div class="ml-10 mt-n6 flex-row justify-space-around">
            <div>
                Just usual meme review like pewds did
            </div>
            <div>
                asdfsdsf
            </div>
        </div>
    </v-container>
</template>

<script>
    export default {
        name: "Channel"
    }
</script>

<style scoped>

</style>
