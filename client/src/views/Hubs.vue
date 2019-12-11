<template>
    <div id="land">
        <v-container>
            <v-col cols="12">
                <router-link to="hubs/gaming">
                    <v-card dark class="mt-1 v-btn" color="#505050" :ripple="true" :hover="true" tile>
                        <div class="d-flex flex-no-wrap justify-space-between">
                            <div>
                                <v-card-title class="headline">Гейминг</v-card-title>
                            </div>
                            <v-avatar class="ma-3 v-btn" height="60" width="90" tile>
                                <v-img src="../assets/gamingHub.png"></v-img>
                            </v-avatar>
                        </div>
                    </v-card>
                </router-link>
                <router-link to="/hubs/creative">
                    <v-card dark class="mt-1 v-btn" color="#505050" :ripple="true" :hover="true" tile>
                        <div class="d-flex flex-no-wrap justify-space-between">
                            <div>
                                <v-card-title class="headline">Креатив</v-card-title>
                            </div>
                            <v-avatar class="ma-3" height="60" width="105" tile>
                                <v-img src="../assets/creativeHub.png"></v-img>
                            </v-avatar>
                        </div>
                    </v-card>
                </router-link>
                <router-link to="/hubs/podcasts">
                    <v-card dark class="mt-1 v-btn" color="#505050" :ripple="true" :hover="true"  tile>
                        <div class="d-flex flex-no-wrap justify-space-between">
                            <div>
                                <v-card-title class="headline">Подкасты</v-card-title>
                            </div>
                            <v-avatar class="ma-3 mr-10" height="60" width="40" min-width="10" tile>
                                <v-img src="../assets/podcastsHub.png"></v-img>
                            </v-avatar>
                        </div>
                    </v-card>
                </router-link>
                <router-link to="/hubs/science">
                    <v-card dark class="mt-1 v-btn" color="#505050" :ripple="true" :hover="true" tile>
                        <div class="d-flex flex-no-wrap justify-space-between">
                            <div>
                                <v-card-title class="headline">Наука и обучение</v-card-title>
                            </div>
                            <v-avatar class="ma-3 mr-8" height="60" width="55" tile>
                                <v-img src="../assets/sciHub.png"></v-img>
                            </v-avatar>
                        </div>
                    </v-card>
                </router-link>
                <router-link to="/hubs/irl">
                    <v-card dark class="mt-1 v-btn" color="#505050" :ripple="true" :hover="true" tile>
                        <div class="d-flex flex-no-wrap justify-space-between">
                            <div>
                                <v-card-title class="headline">IRL</v-card-title>
                            </div>
                            <v-avatar class="ma-3 mr-9" height="60" width="40" min-width="10" tile>
                                <v-img src="../assets/irlHub.png"></v-img>
                            </v-avatar>
                        </div>
                    </v-card>
                </router-link>
                <router-link to="/hubs/etc">
                    <v-card dark class="mt-1 v-btn" color="#505050" :ripple="true" :hover="true" tile>
                        <div class="d-flex flex-no-wrap justify-space-between">
                            <div>
                                <v-card-title class="headline">ETC</v-card-title>
                            </div>
                            <v-avatar class="ma-3" height="60" width="115" tile>
                                <v-img src="../assets/etcHub.png" height="30" width="115"></v-img>
                            </v-avatar>
                        </div>
                    </v-card>
                </router-link>
            </v-col>
        </v-container>
    </div>

</template>

<script>
    export default {
        name: "Hubs"
    }
</script>

<style scoped>
    a{
        text-decoration: none;
    }
</style>
