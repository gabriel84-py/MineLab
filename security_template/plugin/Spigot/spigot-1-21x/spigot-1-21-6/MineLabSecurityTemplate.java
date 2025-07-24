package org.nexko.mineLabSecurityTemplate;

import org.bukkit.plugin.java.JavaPlugin;
import org.nexko.mineLabSecurityTemplate.security.*;
import java.io.File;

public final class MineLabSecurityTemplate extends JavaPlugin {

    private LicenseManager licenseManager;
    private Serverip serverip;
    private Servermac servermac;
    private Pluginbit pluginbit;
    private Hashage hashage;

    @Override
    public void onEnable() {
        //Si la classe check licence n'existe pas, disabled
        try {
            Class.forName("org.nexko.mineLabSecurityTemplate.security.LicenseManager");
        } catch (ClassNotFoundException e) {
            getLogger().severe("LicenseManager class is missing! Plugin is shutting down.");
            getServer().getPluginManager().disablePlugin(this);
            return;
        }

        //Récupérer l'ip et le port du serveur
        serverip = new Serverip();
        String ip = serverip.getip();
        getLogger().info("IP : " + ip);

        //Récupérer l'adresse mac du serveur
        servermac = new Servermac();
        String macAddress = servermac.getMacAddress();
        getLogger().info("Adresse MAC du serveur : " + macAddress);

        //Récupérer la taille du plugin
        pluginbit = new Pluginbit(this);
        double taille = pluginbit.getbitplugin();
        getLogger().info("Taille du plugin : " + taille + " bites");

        //Hasher le tout
        hashage = new Hashage();
        String hash = hashage.hashString(ip + macAddress + taille);
        getLogger().info("Hash : " + hash);

        //Licence Manager
        licenseManager = new LicenseManager();

        //FIN
        getLogger().info("Enabled");
    }

    @Override
    public void onDisable() {
        //FIN
        getLogger().info("Disabled");
    }

    public File getPluginFil() {
        return super.getFile(); // accessible ici car on hérite de JavaPlugin
    }
}
