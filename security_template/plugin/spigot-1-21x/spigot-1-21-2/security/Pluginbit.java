package org.nexko.mineLabSecurityTemplate.security;

import org.bukkit.Bukkit;
import org.nexko.mineLabSecurityTemplate.MineLabSecurityTemplate;

import java.io.File;

public class Pluginbit {

    private MineLabSecurityTemplate plugin;

    public Pluginbit(MineLabSecurityTemplate plugin) {
        this.plugin = plugin;
    }

    public double getbitplugin() {
        File pluginFile = plugin.getPluginFil();

        long sizeBytes = pluginFile.length();
        long sizeBits = sizeBytes * 8;

        if (!pluginFile.exists()) {
            Bukkit.getLogger().warning("Fichier .jar introuvable !");
        }

        return sizeBits;
    }
}