package org.nexko.mineLabSecurityTemplate120.security;

import org.bukkit.Bukkit;
import org.nexko.mineLabSecurityTemplate120.MineLabSecurityTemplate120;

import java.io.File;

public class Pluginbit {

    private MineLabSecurityTemplate120 plugin;

    public Pluginbit(MineLabSecurityTemplate120 plugin) {
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