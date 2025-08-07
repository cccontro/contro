plugins {
    alias(libs.plugins.kotlin.jvm)
    application
    id("com.gradleup.shadow") version "9.0.0-beta17"
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("net.sourceforge.owlapi:owlapi-distribution:5.5.1")
    implementation("net.sourceforge.owlapi:org.semanticweb.hermit:1.4.5.519")
    implementation("ch.qos.logback:logback-classic:1.5.18")
}

application {
    mainClass.set("OntExportKt")
}

tasks.shadowJar {
    archiveBaseName.set("ontexport")
    archiveClassifier.set("") // Remove -all suffix
    archiveVersion.set("")
    mergeServiceFiles()
}

tasks.getByName<Jar>("jar") {
    enabled = false
}