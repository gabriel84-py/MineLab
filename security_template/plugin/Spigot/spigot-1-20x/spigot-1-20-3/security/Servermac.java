package org.nexko.mineLabSecurityTemplate120.security;

import java.net.InetAddress;
import java.net.NetworkInterface;
import java.util.Enumeration;

public class Servermac {

    public String getMacAddress() {
        try {
            InetAddress ip = InetAddress.getLocalHost();
            NetworkInterface network = NetworkInterface.getByInetAddress(ip);

            if (network == null) {
                // Si on n'a pas trouvé l'interface par l'IP locale, on parcourt toutes les interfaces
                Enumeration<NetworkInterface> interfaces = NetworkInterface.getNetworkInterfaces();
                while (interfaces.hasMoreElements()) {
                    NetworkInterface ni = interfaces.nextElement();
                    if (!ni.isLoopback() && ni.getHardwareAddress() != null) {
                        network = ni;
                        break;
                    }
                }
            }

            if (network == null) {
                return "Interface réseau non trouvée.";
            }

            byte[] mac = network.getHardwareAddress();
            if (mac == null) {
                return "Adresse MAC non disponible.";
            }

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < mac.length; i++) {
                sb.append(String.format("%02X%s", mac[i], (i < mac.length - 1) ? "-" : ""));
            }

            return sb.toString();

        } catch (Exception e) {
            return "Erreur : " + e.getMessage();
        }
    }
}