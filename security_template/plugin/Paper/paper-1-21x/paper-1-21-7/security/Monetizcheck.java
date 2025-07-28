package org.nexko.mineLabSecurityTemplate.security;

import org.bukkit.Bukkit;
import org.bukkit.plugin.PluginManager;

import static org.bukkit.Bukkit.getLogger;

public class Monetizcheck {

    public void detectMonetizationPlugins() {
        PluginManager pm = Bukkit.getPluginManager();

        if (pm.getPlugin("BuycraftX") != null) {
            getLogger().info("✔ Tebex (BuycraftX) détecté !");
        }

        if (pm.getPlugin("CraftingStore") != null) {
            getLogger().info("✔ CraftingStore détecté !");
        }

        if (pm.getPlugin("DonationStore") != null) {
            getLogger().info("✔ DonationStore détecté !");
        }

        if (pm.getPlugin("PlayerServers") != null) {
            getLogger().info("✔ PlayerServers détecté !");
        }
    }
}
