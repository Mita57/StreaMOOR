<template>
    <v-container fluid grid-list-xl>
        <v-layout wrap justify-space-around>
            <v-flex v-for="i in 20">
                <v-card class="mx-auto" max-width="344" outlined tile>
                    <v-list-item three-line>
                        <v-list-item-content>
                            <div class="overline mb-4">OVERLINE</div>
                            <v-list-item-title class="headline mb-1">Headline 5</v-list-item-title>
                            <v-list-item-subtitle>Greyhound divisely hello coldly fonwderfully</v-list-item-subtitle>
                        </v-list-item-content>

                        <v-list-item-avatar tile size="80" color="grey"></v-list-item-avatar>
                    </v-list-item>
                    <v-card-actions>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "Channels"
    }
</script>

<style scoped>

</style>
